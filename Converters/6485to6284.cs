using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Text;
using System.Xml;

class Convert6485To6284
{
    // Converts CardXML from patch 1.2 format to pre-1.2 format.
    static void Main(string[] args)
    {
        if (args.Length < 2)
        {
            Console.WriteLine(
                "Usage: {0} [new TextAsset folder] [output folder]",
                Path.GetFileNameWithoutExtension(
                    Process.GetCurrentProcess().MainModule.FileName));
            return;
        }

        var newFolder = args[0];
        var outputFolder = args[1];
        var entities = new Dictionary<string, XmlElement>();
        var locales = new List<string>
        {
            "enUS", "enGB", "zhTW", "zhCN", "ruRU", "ptBR", "ptPT",
            "plPL", "koKR", "itIT", "frFR", "esMX", "esES", "deDE"
        };
        foreach (var locale in locales)
        {
            var filePath = Path.Combine(newFolder, locale + ".txt");
            if (locale.Length != 4)
            {
                continue;
            }
            var doc = new XmlDocument();
            using (var fs = File.Open(filePath, FileMode.Open,
                FileAccess.Read, FileShare.ReadWrite))
            using (var sr = new StreamReader(fs, Encoding.UTF8))
            {
                doc.Load(sr);
                var node = doc.FirstChild;
                while (node.NodeType != XmlNodeType.Element)
                {
                    node = node.NextSibling;
                }
                foreach (var child in node.ChildNodes)
                {
                    var childNode = child as XmlNode;
                    var cardID = childNode.Attributes["CardID"].Value;
                    if (!entities.ContainsKey(cardID))
                    {
                        entities[cardID] = childNode as XmlElement;
                        InitLocaleNodes(entities[cardID], locale);
                    }
                    else
                    {
                        AddLocaleNodes(entities[cardID], childNode as XmlElement, locale);
                    }
                }
            }
        }
        if (!Directory.Exists(outputFolder))
        {
            Directory.CreateDirectory(outputFolder);
        }
        var utf8 = new UTF8();
        var xmlSettings = new XmlWriterSettings
        {
            Indent = true,
            IndentChars = "  ",
            NewLineChars = "\n",
            Encoding = utf8
        };
        foreach (var pair in entities)
        {
            var cardID = pair.Key;
            var entity = pair.Value;
            ReorderFrench(entity, cardID);
            var outPath = Path.Combine(outputFolder, cardID + ".xml");
            using (var fs = File.Open(outPath, FileMode.Create, FileAccess.Write, FileShare.Read))
            using (var sw = new StreamWriter(fs, utf8))
            using (var xw = XmlWriter.Create(sw, xmlSettings))
            {
                xw.WriteStartDocument();
                entity.WriteTo(xw);
                xw.Flush();
            }
        }
    }

    static void TraverseStringTags(XmlElement entity, Action<XmlElement> tagModifier)
    {
        foreach (var child in entity.ChildNodes)
        {
            var childNode = child as XmlNode;
            var childEl = childNode as XmlElement;
            if (childNode == null || childEl == null)
            {
                continue;
            }
            if (childNode.NodeType == XmlNodeType.Element &&
                childNode.Name == "Tag" &&
                childEl.Attributes["type"].Value == "String")
            {
                tagModifier(childEl);
            }
        }
    }

    static XmlElement CreateLocaleNode(XmlElement entity, string locale, string value)
    {
        var localeNode = entity.OwnerDocument.CreateElement(locale);
        localeNode.InnerText = value;
        return localeNode;
    }

    static void InitLocaleNodes(XmlElement entity, string locale)
    {
        TraverseStringTags(entity, (el) =>
        {
            var value = el.InnerText.Replace("\n", "\\n");
            el.InnerXml = "";
            el.AppendChild(CreateLocaleNode(entity, locale, value));
        });
    }

    static void AddLocaleNodes(XmlElement entity, XmlElement newEntity, string locale)
    {
        var values = new Dictionary<string, string>();
        TraverseStringTags(newEntity, (el) =>
        {
            values[el.Attributes["name"].Value] = el.InnerText;
        });
        TraverseStringTags(entity, (el) =>
        {
            var tagName = el.Attributes["name"].Value;
            var value = values[tagName].Replace("\n", "\\n");
            var prevEl = el.LastChild as XmlElement;
            var prevLocale = prevEl.Name;
            var prevValue = prevEl.InnerText;
            if (value != null && value != "" && tagName != "ArtistName" &&
                !(prevLocale == "enUS" && locale == "enGB" && prevValue == value) &&
                !(prevLocale == "ptBR" && locale == "ptPT" && prevValue == value))
            {
                el.AppendChild(CreateLocaleNode(entity, locale, value));
            }
        });
    }

    static void ReorderFrench(XmlElement entity, string cardID)
    {
        if (!frenchBeforeChineseCards.Contains(cardID))
        {
            return;
        }
        TraverseStringTags(entity, (el) =>
        {
            var tagName = el.Attributes["name"].Value;
            if (frenchAfterItalianTags.Contains(tagName) &&
                !(tagName == "TargetingArrowText" &&
                targetingArrowExceptions.Contains(cardID)))
            {
                    return;
            }
            var node = el.FirstChild;
            XmlElement frenchEl = null;
            while (node != null)
            {
                var nextNode = node.NextSibling;
                if (frenchEl == null && node.Name == "frFR")
                {
                    frenchEl = node as XmlElement;
                    el.RemoveChild(frenchEl);
                    nextNode = el.FirstChild;
                }
                if (frenchEl != null && node.Name == "enUS")
                {
                    el.InsertAfter(frenchEl, node);
                    break;
                }
                node = nextNode;
            }
        });
    }

    class UTF8 : UTF8Encoding
    {
        public UTF8()
            : base(false)
        { }

        public override string WebName
        {
            get
            {
                return "UTF-8";
            }
        }
    }

    // Either this or read the old xml!
    static List<string> frenchAfterItalianTags = new List<string>
    {
        "FlavorText", "HowToGetThisGoldCard", "HowToGetThisCard",
        "TargetingArrowText"
    };
    static List<string> targetingArrowExceptions = new List<string>
    {
        "CS2_034", "CS2_042", "CS2_117", "CS2_141", "CS2_150", "CS2_188",
        "CS2_189", "CS2_203", "EX1_005", "EX1_011", "EX1_048",
        "EX1_049", "EX1_057", "EX1_059", "EX1_083", "EX1_091", "EX1_133",
        "EX1_283", "EX1_362", "EX1_564", "EX1_587", "EX1_603", "NEW1_014"
    };
    static List<string> frenchBeforeChineseCards = new List<string>
    {
        "CS1_069", "CS1_112", "CS1_113", "CS1_113e", "CS1_130", "CS1h_001",
        "CS2_003", "CS2_004", "CS2_004e", "CS2_005", "CS2_005o", "CS2_007",
        "CS2_008", "CS2_009", "CS2_009e", "CS2_011", "CS2_011o", "CS2_012",
        "CS2_013", "CS2_017", "CS2_017o", "CS2_022", "CS2_022e", "CS2_023",
        "CS2_024", "CS2_025", "CS2_026", "CS2_028", "CS2_029", "CS2_031", "CS2_032",
        "CS2_033", "CS2_034", "CS2_037", "CS2_038", "CS2_038e", "CS2_039",
        "CS2_041", "CS2_042", "CS2_045", "CS2_045e", "CS2_046", "CS2_046e",
        "CS2_049", "CS2_050", "CS2_051", "CS2_052", "CS2_053", "CS2_056", "CS2_057",
        "CS2_059", "CS2_059o", "CS2_061", "CS2_062", "CS2_063", "CS2_063e",
        "CS2_064", "CS2_065", "CS2_072", "CS2_073", "CS2_073e", "CS2_073e2",
        "CS2_074", "CS2_075", "CS2_076", "CS2_077", "CS2_080", "CS2_082",
        "CS2_083b", "CS2_083e", "CS2_084", "CS2_084e", "CS2_087", "CS2_087e",
        "CS2_089", "CS2_091", "CS2_092", "CS2_092e", "CS2_093", "CS2_094",
        "CS2_097", "CS2_101", "CS2_101t", "CS2_102", "CS2_103e", "CS2_103e2",
        "CS2_104", "CS2_104e", "CS2_105", "CS2_105e", "CS2_106", "CS2_108",
        "CS2_112", "CS2_114", "CS2_117", "CS2_118", "CS2_119", "CS2_120", "CS2_121",
        "CS2_122", "CS2_122e", "CS2_124", "CS2_125", "CS2_127", "CS2_131",
        "CS2_141", "CS2_142", "CS2_146", "CS2_146o", "CS2_147", "CS2_150",
        "CS2_151", "CS2_152", "CS2_155", "CS2_161", "CS2_162", "CS2_168", "CS2_169",
        "CS2_171", "CS2_173", "CS2_179", "CS2_181", "CS2_181e", "CS2_186",
        "CS2_187", "CS2_188", "CS2_188o", "CS2_189", "CS2_196", "CS2_197",
        "CS2_200", "CS2_201", "CS2_203", "CS2_213", "CS2_222", "CS2_222o",
        "CS2_226", "CS2_226o", "CS2_227", "CS2_231", "CS2_232", "CS2_234",
        "CS2_235", "CS2_236", "CS2_236e", "CS2_boar", "CS2_mirror",
        "CS2_tk1", "DREAM_01", "DREAM_02", "DREAM_03", "DREAM_04", "DREAM_05",
        "DREAM_05e", "DS1_055", "DS1_070", "DS1_070o", "DS1_175", "DS1_175o",
        "DS1_178", "DS1_178e", "DS1_184", "DS1_185", "DS1_188", "DS1_233",
        "DS1h_292", "EX1_001", "EX1_001e", "EX1_002", "EX1_004e", "EX1_005",
        "EX1_006", "EX1_007", "EX1_008", "EX1_009", "EX1_010", "EX1_011", "EX1_012",
        "EX1_014", "EX1_014t", "EX1_014te", "EX1_015", "EX1_019e", "EX1_020",
        "EX1_021", "EX1_023", "EX1_025", "EX1_025t", "EX1_028", "EX1_029",
        "EX1_032", "EX1_033", "EX1_043", "EX1_043e", "EX1_046e", "EX1_048",
        "EX1_049", "EX1_050", "EX1_055", "EX1_055o", "EX1_057", "EX1_058",
        "EX1_059", "EX1_059e", "EX1_059e2", "EX1_066", "EX1_067", "EX1_076",
        "EX1_082", "EX1_083", "EX1_084", "EX1_084e", "EX1_089", "EX1_091",
        "EX1_091o", "EX1_093", "EX1_093e", "EX1_095", "EX1_096", "EX1_100",
        "EX1_102", "EX1_103", "EX1_103e", "EX1_105", "EX1_110", "EX1_110t",
        "EX1_116", "EX1_124", "EX1_126", "EX1_128", "EX1_129", "EX1_130a",
        "EX1_131", "EX1_131t", "EX1_132", "EX1_133", "EX1_134", "EX1_136",
        "EX1_137", "EX1_144", "EX1_145", "EX1_154", "EX1_154a",
        "EX1_154b", "EX1_155", "EX1_155a", "EX1_155ae", "EX1_155b", "EX1_155be",
        "EX1_158", "EX1_158e", "EX1_158t", "EX1_160", "EX1_160a", "EX1_160b",
        "EX1_160be", "EX1_160t", "EX1_161", "EX1_161o", "EX1_162o", "EX1_164",
        "EX1_164a", "EX1_164b", "EX1_165", "EX1_165a", "EX1_165b", "EX1_165t1",
        "EX1_165t2", "EX1_166", "EX1_166a", "EX1_166b", "EX1_169", "EX1_170",
        "EX1_173", "EX1_178", "EX1_178a", "EX1_178ae", "EX1_178b", "EX1_178be",
        "EX1_238", "EX1_241", "EX1_243", "EX1_244", "EX1_244e", "EX1_245",
        "EX1_246", "EX1_246e", "EX1_247", "EX1_249", "EX1_250", "EX1_251",
        "EX1_258", "EX1_259", "EX1_275", "EX1_277", "EX1_279", "EX1_283", "EX1_284",
        "EX1_287", "EX1_289", "EX1_294", "EX1_295", "EX1_295o", "EX1_298",
        "EX1_301", "EX1_302", "EX1_303", "EX1_304", "EX1_304e", "EX1_308",
        "EX1_309", "EX1_310", "EX1_312", "EX1_313", "EX1_315", "EX1_316",
        "EX1_316e", "EX1_317", "EX1_319", "EX1_320", "EX1_323", "EX1_323h",
        "EX1_323w", "EX1_332", "EX1_334", "EX1_335", "EX1_339", "EX1_341",
        "EX1_349", "EX1_350", "EX1_354", "EX1_355", "EX1_355e", "EX1_360",
        "EX1_360e", "EX1_362", "EX1_363", "EX1_363e", "EX1_363e2", "EX1_365",
        "EX1_366", "EX1_366e", "EX1_371", "EX1_379", "EX1_379e", "EX1_382",
        "EX1_383", "EX1_384", "EX1_390", "EX1_391", "EX1_392", "EX1_396", "EX1_398",
        "EX1_398t", "EX1_399", "EX1_399e", "EX1_400", "EX1_402", "EX1_405",
        "EX1_407", "EX1_408", "EX1_409", "EX1_409e", "EX1_409t", "EX1_410",
        "EX1_411", "EX1_411e", "EX1_412", "EX1_414", "EX1_506a", "EX1_507",
        "EX1_507e", "EX1_508", "EX1_508o", "EX1_509", "EX1_509e", "EX1_522",
        "EX1_531", "EX1_531e", "EX1_536e", "EX1_537", "EX1_538", "EX1_538t",
        "EX1_539", "EX1_543", "EX1_544", "EX1_549", "EX1_549o", "EX1_554",
        "EX1_554t", "EX1_556", "EX1_557", "EX1_558", "EX1_559", "EX1_560",
        "EX1_561", "EX1_562", "EX1_563", "EX1_564", "EX1_565o", "EX1_567",
        "EX1_570", "EX1_570e", "EX1_571", "EX1_572", "EX1_573", "EX1_573a",
        "EX1_573ae", "EX1_573b", "EX1_573t", "EX1_577", "EX1_578", "EX1_581",
        "EX1_582", "EX1_583", "EX1_584", "EX1_584e", "EX1_586", "EX1_587",
        "EX1_590", "EX1_590e", "EX1_591", "EX1_593", "EX1_594", "EX1_595",
        "EX1_596", "EX1_596e", "EX1_598", "EX1_603", "EX1_603e",
        "EX1_604", "EX1_604o", "EX1_606", "EX1_607", "EX1_607e", "EX1_608",
        "EX1_609", "EX1_610", "EX1_611", "EX1_611e", "EX1_612", "EX1_612o",
        "EX1_613", "EX1_613e", "EX1_614", "EX1_616", "EX1_619", "EX1_619e",
        "EX1_620", "EX1_621", "EX1_623", "EX1_624", "EX1_625",
        "EX1_625t", "EX1_625t2", "EX1_626", "EX1_finkle", "EX1_tk11", "EX1_tk28",
        "EX1_tk29", "EX1_tk31", "EX1_tk33", "EX1_tk34", "EX1_tk9", "HERO_01", "HERO_04",
        "NEW1_004", "NEW1_005", "NEW1_006", "NEW1_007", "NEW1_007a", "NEW1_007b",
        "NEW1_008", "NEW1_008a", "NEW1_008b", "NEW1_009", "NEW1_010", "NEW1_011",
        "NEW1_012", "NEW1_012o", "NEW1_014", "NEW1_017", "NEW1_017e", "NEW1_018",
        "NEW1_018e", "NEW1_019", "NEW1_020", "NEW1_021", "NEW1_023", "NEW1_024",
        "NEW1_024o", "NEW1_025", "NEW1_025e", "NEW1_026", "NEW1_026t", "NEW1_029",
        "NEW1_030", "NEW1_031", "NEW1_032", "NEW1_033", "NEW1_033o", "NEW1_034",
        "NEW1_036", "NEW1_036e", "NEW1_036e2", "NEW1_037", "NEW1_037e", "NEW1_040",
        "NEW1_040t", "NEW1_041", "TU4a_001", "TU4a_002", "TU4a_004", "TU4a_006",
        "TU4b_001", "TU4c_001", "TU4c_002", "TU4c_003", "TU4c_004", "TU4c_005",
        "TU4c_006", "TU4c_006e", "TU4c_007", "TU4c_008", "TU4c_008e", "TU4d_001",
        "TU4d_002", "TU4d_003", "TU4e_001", "TU4e_002", "TU4e_002t", "TU4e_003",
        "TU4e_004", "TU4e_005", "TU4e_007", "TU4f_001", "TU4f_002", "TU4f_003",
        "TU4f_004", "TU4f_004o", "TU4f_005", "TU4f_006", "TU4f_006o",
        "ds1_whelptoken", "hexfrog", "skele11", "skele21", "tt_010", "tt_010a"
    };
}
