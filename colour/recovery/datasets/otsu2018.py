# -*- coding: utf-8 -*-
"""
Otsu et al. (2018) - Reflectance Recovery
=========================================

Defines the datasets for reflectance recovery using *Otsu et al. (2018)*
method.

References
----------
-   :cite:`Otsu2018` : Otsu, H., Yamamoto, M. & Hachisuka, T. (2018)
    Reproducing Spectral Reflectances From Tristimulus Colours. Computer
    Graphics Forum. 37(6), 370–381. doi:10.1111/cgf.13332
"""

import numpy as np
from colour.colorimetry import SpectralShape

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2013-2020 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-developers@colour-science.org'
__status__ = 'Production'

OTSU_2018_SPECTRAL_SHAPE = SpectralShape(380, 730, 10)
"""
The spectral shape of *Otsu et al. (2018)* basis functions and means.

References
----------
:cite:`Otsu2018`

OTSU_2018_SPECTRAL_SHAPE : SpectralShape
"""

OTSU_2018_BASIS_FUNCTIONS = np.array([[
    [
        0.033359794,
        0.069816766,
        0.145858662,
        0.208587748,
        0.225045781,
        0.230260467,
        0.23468649,
        0.237479132,
        0.237922746,
        0.235743337,
        0.230636966,
        0.224868019,
        0.220538851,
        0.214245998,
        0.205011936,
        0.194449589,
        0.182172137,
        0.16675381,
        0.149673107,
        0.13588466,
        0.127383558,
        0.121562634,
        0.115070543,
        0.110303774,
        0.108658862,
        0.110404095,
        0.11413349,
        0.118971322,
        0.123157804,
        0.123054245,
        0.119622289,
        0.116466163,
        0.114699356,
        0.115051812,
        0.1180796,
        0.125700322,
    ],
    [
        -0.015712659,
        -0.036497435,
        -0.083631104,
        -0.123972215,
        -0.129432141,
        -0.113757935,
        -0.074978412,
        -0.023837819,
        0.051049315,
        0.138878712,
        0.218967535,
        0.278285048,
        0.297475087,
        0.286292061,
        0.25783095,
        0.206696101,
        0.144324772,
        0.085519078,
        0.038286146,
        0.001619797,
        -0.035117557,
        -0.072027247,
        -0.096533704,
        -0.103087741,
        -0.102368364,
        -0.114391855,
        -0.139967122,
        -0.171162687,
        -0.196658516,
        -0.207454048,
        -0.204801733,
        -0.203879004,
        -0.213328289,
        -0.22895892,
        -0.241698598,
        -0.25146479,
    ],
    [
        -0.020337631,
        -0.053622913,
        -0.122405706,
        -0.179462494,
        -0.200564443,
        -0.23233224,
        -0.283247005,
        -0.304278573,
        -0.276059936,
        -0.220589316,
        -0.139053387,
        -0.046042855,
        0.031991873,
        0.10337266,
        0.170370407,
        0.214905881,
        0.240971387,
        0.254238542,
        0.255631209,
        0.238008218,
        0.209534818,
        0.177808852,
        0.15309531,
        0.139956117,
        0.131477876,
        0.116280805,
        0.095933679,
        0.075698905,
        0.0659778,
        0.069857488,
        0.08298836,
        0.090329558,
        0.082929925,
        0.067734041,
        0.05324286,
        0.041115251,
    ],
], [
    [
        -0.022574277173862713,
        -0.04580454714541371,
        -0.089540336581154192,
        -0.12005530771055017,
        -0.12563459701293636,
        -0.12595333439645837,
        -0.12670444234219508,
        -0.12715705435395483,
        -0.12913057707506276,
        -0.13354123002336557,
        -0.13855666514343304,
        -0.14308799991330715,
        -0.14951791383958515,
        -0.15845145652482151,
        -0.16495787527646999,
        -0.16781427384520564,
        -0.17170232277018521,
        -0.18042142403466258,
        -0.18962359564086589,
        -0.19407674590552579,
        -0.19587634795792669,
        -0.19670397522552724,
        -0.19619975275648865,
        -0.19518165653001343,
        -0.1940391399425867,
        -0.19368980706846228,
        -0.1927703594174372,
        -0.19234347800755142,
        -0.19207998789953343,
        -0.1918349989217025,
        -0.19191989052413799,
        -0.19216208684132857,
        -0.1927300443475902,
        -0.19273134081681903,
        -0.19197345910434815,
        -0.19195334021916627,
    ],
    [
        -0.021905247198763668,
        -0.047895856196703182,
        -0.10618234949979,
        -0.15900405113964777,
        -0.17702417653425023,
        -0.18536131560391853,
        -0.19315079255300505,
        -0.20224319049559464,
        -0.21765026428606477,
        -0.24359160942259997,
        -0.27299579285349473,
        -0.29049279880094941,
        -0.28346659709985672,
        -0.24283365807615256,
        -0.19188028232791318,
        -0.15475085829598653,
        -0.12084943547312378,
        -0.07129023972829869,
        -0.01545410159994778,
        0.028557978278598323,
        0.063326560262252932,
        0.095563459742963305,
        0.12304807393347031,
        0.14150866887002808,
        0.1518805710409159,
        0.15797342142055862,
        0.16213144452203984,
        0.16563351215078684,
        0.16485760626112306,
        0.1599118854790621,
        0.15381118424011236,
        0.14657408643195061,
        0.14252150862995686,
        0.14149924680385922,
        0.14426259164189553,
        0.14568116947965443,
    ],
    [
        0.038621925933278435,
        0.086079778929663842,
        0.18758937472970783,
        0.2638028734446175,
        0.27264656532342524,
        0.26415033785924025,
        0.25431550822206783,
        0.24061274238989599,
        0.21646081169191303,
        0.16375249929345426,
        0.065405943906418268,
        -0.057489571474714611,
        -0.16090875920779929,
        -0.22967562960590965,
        -0.28665433153182635,
        -0.32394421018597008,
        -0.31885416680273615,
        -0.26443039994661971,
        -0.19096541067598802,
        -0.13794182744763242,
        -0.09283207180313692,
        -0.048638278090540624,
        -0.007057011946489793,
        0.025908644910288447,
        0.045168125892492098,
        0.055433406852733874,
        0.062648667057779273,
        0.069997973640360922,
        0.072857470083200482,
        0.068521304598552782,
        0.05932205006228336,
        0.047344248467979202,
        0.034569705940415876,
        0.028544123201231449,
        0.031571972291487678,
        0.033591223715048073,
    ],
], [
    [
        -0.027092800961875659,
        -0.05686223110461408,
        -0.10035667073983964,
        -0.11655686561575981,
        -0.11422957067657943,
        -0.11025418465506862,
        -0.10767542796968975,
        -0.10388290237276118,
        -0.1015822584891887,
        -0.10042808265232403,
        -0.094443911576461148,
        -0.085397186711102649,
        -0.081403517164651426,
        -0.078998363668626767,
        -0.070923617868227734,
        -0.06431797115426903,
        -0.065511300335222719,
        -0.074493415170754931,
        -0.081083618898088003,
        -0.090894421292060143,
        -0.12404701968906916,
        -0.1678633272894792,
        -0.20250158743930527,
        -0.22377717318551535,
        -0.23406228761612988,
        -0.2402328639520801,
        -0.24230652318518972,
        -0.24409552662937148,
        -0.24451095295280248,
        -0.24396897026804176,
        -0.24334193238409188,
        -0.24303731113979424,
        -0.24384555693930871,
        -0.24439637959579152,
        -0.24397837395728775,
        -0.24435930927502705,
    ],
    [
        0.020011486010201151,
        0.048998416580494086,
        0.091102316994959076,
        0.10753208990080826,
        0.098470673418214458,
        0.097025565098797756,
        0.1031615612097386,
        0.10877098463664207,
        0.11985177404764036,
        0.13576834462543336,
        0.14149065311281014,
        0.13685946675439886,
        0.13973613295200196,
        0.14909977184067982,
        0.14654199509091873,
        0.14130994015312165,
        0.14757252813883043,
        0.18077817300610374,
        0.21009387986393199,
        0.23369907594299305,
        0.29227081282780004,
        0.31933306627506691,
        0.26565290061291041,
        0.17228196686094716,
        0.076390272591150915,
        -0.0029229184058072641,
        -0.061428003182239732,
        -0.10401144539762601,
        -0.13589472821785523,
        -0.15816114518317095,
        -0.17335642699648807,
        -0.18902786670833094,
        -0.20610333417513085,
        -0.22242224746425526,
        -0.23664147979214531,
        -0.24998288325425144,
    ],
    [
        -0.018604888523577168,
        -0.06851902564207997,
        -0.21326717698986006,
        -0.30102165576283019,
        -0.31649926306090304,
        -0.30060756567987956,
        -0.27084117252238304,
        -0.2342591277814256,
        -0.20338041193211276,
        -0.17461428657405265,
        -0.14854465986513404,
        -0.12781379545378718,
        -0.11230428006257434,
        -0.087975844820372906,
        -0.055376996192055446,
        -0.030898750669759362,
        -0.027435027144774037,
        -0.015788021006403977,
        -0.002052727483851931,
        0.010090068318085881,
        0.080982969286818154,
        0.21731539216862897,
        0.31846566331995801,
        0.32348510302323596,
        0.26108337233732459,
        0.1870588914854851,
        0.1197358497294002,
        0.06706555745724066,
        0.031243265262699445,
        0.0079226523029403816,
        -0.0037996253399519612,
        -0.019808511489877285,
        -0.038216435631261328,
        -0.061662766366106687,
        -0.080033159465559625,
        -0.096979974515244455,
    ],
], [
    [
        0.026768243041886113,
        0.059464074759657821,
        0.12900702308575138,
        0.17092577830538522,
        0.17433273953929146,
        0.16835540326878368,
        0.15826424805464265,
        0.14647224313786575,
        0.1346026304079895,
        0.12159264960543423,
        0.10837126623117754,
        0.095459380361891485,
        0.084546573726778235,
        0.075030597156375223,
        0.064967403457589792,
        0.056388543099616571,
        0.054084978457088866,
        0.055437352570434723,
        0.05555858715239536,
        0.057595838797090175,
        0.063452890564987499,
        0.073218409530731499,
        0.093940174606657378,
        0.12959719899113231,
        0.1734841595045358,
        0.21285437318563405,
        0.23979589047651886,
        0.25571215090479932,
        0.26147369410179094,
        0.26060735062830592,
        0.25695755826517525,
        0.25495084519503508,
        0.25508140335236734,
        0.25382248374599431,
        0.25315232973604851,
        0.25321847259615987,
    ],
    [
        -0.018737448479402168,
        -0.059908993264420694,
        -0.13587937041765039,
        -0.19250932779711649,
        -0.21685711379342484,
        -0.23833290753023634,
        -0.25940907727956292,
        -0.27129217353501439,
        -0.27152046701232635,
        -0.25903073272885363,
        -0.23448070616812938,
        -0.19749538078381751,
        -0.16551798851884006,
        -0.14072688005214101,
        -0.11914770422601269,
        -0.11063268885678886,
        -0.10948247432054088,
        -0.1094333638968575,
        -0.10553405777913306,
        -0.10897919714631589,
        -0.11556837510924602,
        -0.12678816534296078,
        -0.12909988927091548,
        -0.092858889557997079,
        -0.0094986658060967431,
        0.063012500347605249,
        0.1064698574510137,
        0.12256333095253447,
        0.13523848767144181,
        0.14386501113297953,
        0.15441065150742014,
        0.16682910934595863,
        0.17982703518357265,
        0.19629872698899911,
        0.20993169814916909,
        0.22283191255022117,
    ],
    [
        0.006877990961728339,
        0.0063298223619046344,
        -0.016300247253368486,
        -0.054157786495748324,
        -0.07289153491194883,
        -0.085454890006052192,
        -0.090467894365318338,
        -0.080720154767858904,
        -0.070253935622839617,
        -0.056674297718920824,
        -0.040430149674538743,
        -0.018762755090685587,
        -0.0024890726748911175,
        0.004999851798740994,
        0.0071966661367148747,
        0.0014112375950132896,
        0.0013866049217290822,
        0.0041273085546675373,
        0.0049254427451994147,
        0.0086392765226695027,
        0.017682647142245243,
        0.027007678278437242,
        0.053587573063484606,
        0.12515958723848053,
        0.24428784772611917,
        0.34242457928205289,
        0.38094858322069408,
        0.35070697286866737,
        0.25959544573108218,
        0.13920978087352909,
        0.0065571240411875882,
        -0.11671906463074669,
        -0.21483468555348154,
        -0.28912185847014771,
        -0.34279486721072366,
        -0.38307271805096821,
    ],
], [
    [
        -0.021196748367387556,
        -0.045914416027014182,
        -0.10481010401668686,
        -0.16258395638429893,
        -0.17889545337044299,
        -0.18072228226884079,
        -0.18112664009792892,
        -0.1803243472063151,
        -0.17971618615047016,
        -0.17871153535087211,
        -0.17563285652502023,
        -0.1711980839106329,
        -0.16853689988040146,
        -0.16561345617512713,
        -0.16019419889858222,
        -0.15573208563516067,
        -0.15491795255226662,
        -0.15656042280911464,
        -0.15661531826131711,
        -0.15764891623922786,
        -0.16300024791746612,
        -0.1690240752417124,
        -0.17285036097124651,
        -0.17473874057599853,
        -0.17535320823704051,
        -0.17679028377314515,
        -0.17819373966686389,
        -0.18018711283913955,
        -0.18137104389357972,
        -0.18095677225518114,
        -0.18017559421686788,
        -0.17972235196479699,
        -0.17972279615663084,
        -0.17977929580104804,
        -0.1799601449461285,
        -0.181166768923569,
    ],
    [
        0.0036106183889043977,
        0.0040383224476675042,
        0.0089096296964888966,
        0.035248157079807885,
        0.05694248722530626,
        0.072843282192699699,
        0.089296857030450941,
        0.10884229731927056,
        0.12746765305849969,
        0.14422870726029338,
        0.16634052273914524,
        0.18968300551257519,
        0.20235756903744331,
        0.2118737799214325,
        0.23160746600613533,
        0.24467573264157011,
        0.23387224613948968,
        0.20772756148326568,
        0.18558478756428221,
        0.1553725793546254,
        0.088708554185330218,
        0.011772973492821604,
        -0.054889976709800503,
        -0.1070079515114554,
        -0.14115288511720003,
        -0.16117542399322698,
        -0.17218230632555048,
        -0.18073298721042264,
        -0.18906539182769619,
        -0.20004311114038048,
        -0.21240795927734304,
        -0.22370131442259125,
        -0.22996533792354246,
        -0.23257699977177257,
        -0.23162059375757346,
        -0.22709792076398444,
    ],
    [
        0.026485121929555995,
        0.062586887577242317,
        0.14234632723786383,
        0.21547368046916726,
        0.24347885216491971,
        0.24958734564816068,
        0.24081448101006372,
        0.22418376109960433,
        0.19465144188536176,
        0.15445250087507756,
        0.11514475901976122,
        0.073512503277158345,
        0.025351695232522294,
        -0.023990416398060543,
        -0.054838241031072175,
        -0.069221495471924549,
        -0.093315369459094341,
        -0.14508948941010041,
        -0.19321726430075248,
        -0.22742341157660259,
        -0.27490607958077012,
        -0.29854536089141326,
        -0.28507620653536159,
        -0.25817167239338712,
        -0.23466391476319501,
        -0.19576301983826125,
        -0.1373399037939006,
        -0.072193802454370459,
        -0.014907622259105243,
        0.025452503610320958,
        0.04811592885693794,
        0.065428450204223762,
        0.084559689940918711,
        0.10445141018651627,
        0.1219529996380162,
        0.14191426767047791,
    ],
], [
    [
        0.029499050763487134,
        0.053801144928306177,
        0.080795551408645569,
        0.086734611772229686,
        0.082283444778604289,
        0.07805333953848162,
        0.076580661458096791,
        0.074263324654086499,
        0.073687508184255721,
        0.074976744744700438,
        0.071867477321337955,
        0.06522606040102924,
        0.064034482042081037,
        0.06747959315712472,
        0.064200250968631828,
        0.058570996065945076,
        0.061544833681319265,
        0.084329799131897587,
        0.12590749478955982,
        0.16082638200698035,
        0.19171530712010598,
        0.21543531303958838,
        0.22759452497177649,
        0.23276904041357468,
        0.2342736758543584,
        0.23511801139892841,
        0.23630540140724776,
        0.23765549341378889,
        0.23815849278526871,
        0.23735655259306632,
        0.23776190401926256,
        0.2390160236178972,
        0.23966837305669569,
        0.23992004299222611,
        0.2396383723971636,
        0.2405597459348236,
    ],
    [
        -0.057493176903905097,
        -0.10889049665477113,
        -0.16808106208696935,
        -0.18188449289155134,
        -0.17213928808785378,
        -0.16248122054252026,
        -0.15940007865141995,
        -0.15446135954382603,
        -0.15394359073226441,
        -0.15955177134499235,
        -0.15476803378874412,
        -0.14270086430739456,
        -0.14150192246537266,
        -0.15299122361377698,
        -0.1465902421518602,
        -0.132803645212104,
        -0.13654216732616947,
        -0.18711606479886939,
        -0.27646809095728458,
        -0.33376341079739913,
        -0.31149240794382088,
        -0.21605192415199054,
        -0.088722614417590315,
        0.015017164453222829,
        0.074595642022440761,
        0.10463473412925806,
        0.12001248564282355,
        0.12979112919629543,
        0.13792378105731262,
        0.14268404174686664,
        0.14677817922155648,
        0.15510473763112062,
        0.16050632288055705,
        0.16731616487345491,
        0.17324998571439973,
        0.17991527864215207,
    ],
    [
        -0.082444360896071739,
        -0.15336030301728437,
        -0.24426622711321333,
        -0.26384931585866828,
        -0.2489285736644698,
        -0.23077245427661355,
        -0.22241952671928703,
        -0.2035455324750147,
        -0.19616122335466987,
        -0.1907993806896551,
        -0.17229835840027194,
        -0.14208870523710324,
        -0.12630253767591793,
        -0.10363604991038586,
        -0.072019682195322815,
        -0.053128868438094112,
        -0.04004075771120371,
        -0.00053440568762490803,
        0.16020422722625777,
        0.40718001627624578,
        0.4163947024386479,
        0.27850647135244561,
        0.1447037476231347,
        0.042815356508891199,
        -0.010405879954624919,
        -0.03113779622382366,
        -0.035880054428051152,
        -0.038339247330565915,
        -0.035183561990387802,
        -0.023137563815885758,
        -0.022038706581639086,
        -0.029677820082597343,
        -0.02175113614544999,
        -0.016134690184071633,
        -0.013675555885452249,
        -0.011582196403702297,
    ],
], [
    [
        0.018706954425900275,
        0.035691615790370786,
        0.048092680540135123,
        0.048886946548580508,
        0.045788081960323593,
        0.04344586049591366,
        0.043256855709944836,
        0.042221897717230575,
        0.040556810875752851,
        0.040281802077812345,
        0.037605741005674355,
        0.033414498653321474,
        0.030522879769953815,
        0.030072542253092544,
        0.028109817708118812,
        0.025232221777797215,
        0.025386613387815712,
        0.028669472143542769,
        0.038075716315780883,
        0.057721332463509245,
        0.10170369006245189,
        0.16294646278543309,
        0.20902545675000525,
        0.23926676595591634,
        0.25599658226130739,
        0.26216124571088945,
        0.26294121758247357,
        0.26471231240392479,
        0.26430141917656441,
        0.26240021240987121,
        0.26487052223495711,
        0.26522291338114623,
        0.26660542213939931,
        0.26541584484337871,
        0.2639054773713676,
        0.26275220730492782,
    ],
    [
        -0.059259648583802865,
        -0.092956955359335389,
        -0.11130621819722603,
        -0.10992697128373242,
        -0.10115389795872447,
        -0.095955153432515081,
        -0.09677723424692862,
        -0.096060382543489697,
        -0.097366702412065742,
        -0.099922029449187488,
        -0.097043830931807865,
        -0.090020792225387572,
        -0.086733520466911865,
        -0.085577701472653686,
        -0.080640002469695549,
        -0.0791364512157815,
        -0.082718076854233991,
        -0.098073619378134302,
        -0.11457149326572891,
        -0.14765147379188692,
        -0.23874210320885786,
        -0.36798022743083686,
        -0.43048231090135342,
        -0.35215701510596309,
        -0.19641466614055952,
        -0.059138388314848321,
        0.026355189024417185,
        0.078346882716145386,
        0.11384481744795055,
        0.13409102253165275,
        0.14769925378529281,
        0.16322353175604573,
        0.18252922264663107,
        0.20305737442069113,
        0.22128357114965899,
        0.23621196298998062,
    ],
    [
        0.11512389978331515,
        0.22413006962808238,
        0.31954389282025103,
        0.32586304644263525,
        0.30397127558670756,
        0.28352212433907487,
        0.26492834051113151,
        0.24455825069511528,
        0.23050435252217924,
        0.21847071243995733,
        0.19137596848708158,
        0.1601974232892982,
        0.13917066569959388,
        0.11837326624126067,
        0.090039681130961238,
        0.070531803625000222,
        0.066336044816870693,
        0.057517261745436678,
        0.010888354724719695,
        -0.038538433600120839,
        -0.082544535562035767,
        -0.10202561217467844,
        -0.14265191289777529,
        -0.2081131167290538,
        -0.22597980923018762,
        -0.16968023714155689,
        -0.091887925602399972,
        -0.034763584581534696,
        0.005819524832624893,
        0.027732580683770058,
        0.011509366675218666,
        0.011757632392487491,
        0.036727927025401459,
        0.073682755318237106,
        0.10450314791523628,
        0.13170821119526419,
    ],
], [
    [
        -0.01391512397332992,
        -0.023556165803701568,
        -0.032179746895275751,
        -0.033897136230447739,
        -0.033010362813638332,
        -0.032853543714237148,
        -0.033775405487069948,
        -0.034896806312349503,
        -0.03685746938516745,
        -0.040797455645242994,
        -0.045928555263250466,
        -0.052524095733720799,
        -0.064858816417801626,
        -0.088721509983924751,
        -0.12062905249920253,
        -0.14663172901574814,
        -0.16374285973859237,
        -0.17854545670524613,
        -0.19285090669470276,
        -0.20310119935107607,
        -0.20944935602779791,
        -0.21419896526525989,
        -0.21710861272899887,
        -0.21862667803330973,
        -0.22006016766927428,
        -0.2221507734460183,
        -0.22323849303277751,
        -0.22463343282950998,
        -0.22589338966445646,
        -0.22594179947730525,
        -0.22663921592189393,
        -0.22783675444090351,
        -0.22865193500586228,
        -0.22945714446182908,
        -0.22963380305061912,
        -0.23154386034935404,
    ],
    [
        -0.023728764007968396,
        -0.038051268260632432,
        -0.049159519147150221,
        -0.047746262065333611,
        -0.04297236442671773,
        -0.038481156014283036,
        -0.033976425657995399,
        -0.027608031107307258,
        -0.020427164769555053,
        -0.0085247890802179326,
        0.014089372452365129,
        0.046759283321778151,
        0.090052684016265191,
        0.15996855175372468,
        0.27983350884234798,
        0.40454760673506523,
        0.46557425740279146,
        0.42988255821256582,
        0.30040479908227047,
        0.1601614724263957,
        0.06193514273781868,
        -0.0063415852503927398,
        -0.055917288088158351,
        -0.088016143692980636,
        -0.10645480712256676,
        -0.11439528123368227,
        -0.12148762118556097,
        -0.12853160184622442,
        -0.13211749271913961,
        -0.13124291058777687,
        -0.12758412629342486,
        -0.12246334197729329,
        -0.11696553437732297,
        -0.1153812227070585,
        -0.11848205894639263,
        -0.12091688597538751,
    ],
    [
        0.13614121087578832,
        0.221631727478387,
        0.29458621263180562,
        0.30561224752530813,
        0.29501884928368216,
        0.28598447595430682,
        0.28333441324709346,
        0.27912705630178736,
        0.27528060133650206,
        0.27037172224265682,
        0.25595129646913195,
        0.2311211869222273,
        0.20491022536680245,
        0.18294409783499188,
        0.091675757284674614,
        -0.03963638360275884,
        -0.11054285410554264,
        -0.073734587121219955,
        0.026839538961491556,
        0.068701964570249616,
        0.050131369708965055,
        0.023562628763353001,
        0.0025888487047116679,
        -0.0053403867424643295,
        -0.011816440340678774,
        -0.018904029971987882,
        -0.024015526092765162,
        -0.030390728842743943,
        -0.036975438247467143,
        -0.043720790687193485,
        -0.055262504463427155,
        -0.065183851844669821,
        -0.079787372245721563,
        -0.090353777514548247,
        -0.094857142235921857,
        -0.097999628029961802,
    ],
]])
"""
Basis functions for *Otsu et al. (2018)*. This is a list of eight np.arrays,
with one for entry for each cluster. Each np.array contains three basis
functions, quantised with accordance to ``OTSU_2018_SPECTRAL_SHAPE``.

References
----------
:cite:`Otsu2018`

OTSU_2018_BASIS_FUNCTIONS : ndarray
"""

OTSU_2018_MEANS = np.array([[
    0.10085069182389943,
    0.14557836477987415,
    0.21618955974842774,
    0.26241761006289305,
    0.27539660377358477,
    0.28531383647798736,
    0.29863773584905656,
    0.30855169811320765,
    0.31710716981132059,
    0.32332276729559734,
    0.32056880503144641,
    0.30730465408805036,
    0.29085635220125783,
    0.26974641509433944,
    0.24537761006289302,
    0.22229106918238989,
    0.20037320754716983,
    0.17840641509433955,
    0.15444679245283027,
    0.14225157232704402,
    0.13367911949685529,
    0.12840981132075477,
    0.12297345911949682,
    0.11905270440251571,
    0.11778465408805038,
    0.11974377358490564,
    0.12402981132075469,
    0.12976943396226415,
    0.13483974842767291,
    0.13579132075471703,
    0.13499685534591194,
    0.13219408805031446,
    0.13386704402515726,
    0.13686591194968545,
    0.14213257861635226,
    0.15195597484276738,
], [
    0.099739962412408803,
    0.13832746329562026,
    0.19263781475547445,
    0.22097216947810219,
    0.2249150095036497,
    0.2258426793248175,
    0.22858438229562053,
    0.23144331213138686,
    0.2394419671459854,
    0.25520659802554735,
    0.27474755001824847,
    0.29176247448175174,
    0.30942757119707986,
    0.32833185188321135,
    0.34152471104014598,
    0.34492205800000048,
    0.34524719568978096,
    0.3500697162153284,
    0.35226373910948888,
    0.3525736619452553,
    0.34635072814963563,
    0.33788450155109495,
    0.32730242764963524,
    0.31817969820072978,
    0.31196273630291999,
    0.30864278988686139,
    0.30511056795255503,
    0.30259412779197087,
    0.30141088878467137,
    0.30166522981386845,
    0.30447054271897822,
    0.30566773899999983,
    0.30979884475912473,
    0.31087716667883208,
    0.30918824107664239,
    0.30983656317883246,
], [
    0.10163148148148149,
    0.13874148148148155,
    0.18048629629629634,
    0.19058296296296293,
    0.18498296296296293,
    0.17870703703703697,
    0.17455444444444446,
    0.16798407407407415,
    0.16265481481481481,
    0.15838185185185186,
    0.14838851851851853,
    0.13549851851851852,
    0.12967518518518517,
    0.12491777777777781,
    0.11482962962962959,
    0.10857518518518521,
    0.11038555555555557,
    0.11997444444444444,
    0.1255766666666667,
    0.1389977777777778,
    0.1829840740740741,
    0.24777518518518515,
    0.3039033333333333,
    0.34408296296296298,
    0.37026074074074061,
    0.38781962962962946,
    0.39744703703703704,
    0.4043059259259259,
    0.40855074074074083,
    0.4102244444444445,
    0.4122925925925926,
    0.41340555555555564,
    0.41682222222222221,
    0.41964370370370369,
    0.42174666666666671,
    0.42481148148148135,
], [
    0.10518588235294116,
    0.15928000000000003,
    0.23761058823529413,
    0.27525764705882355,
    0.2782,
    0.26746470588235294,
    0.24924588235294115,
    0.22593176470588236,
    0.20151176470588236,
    0.1787235294117647,
    0.1563835294117647,
    0.13379058823529413,
    0.1176858823529412,
    0.10634235294117647,
    0.095734117647058831,
    0.088314117647058821,
    0.085778823529411768,
    0.086729411764705874,
    0.086877647058823532,
    0.087945882352941179,
    0.09118941176470588,
    0.098662352941176465,
    0.11569764705882354,
    0.14323176470588234,
    0.1737258823529412,
    0.20689176470588236,
    0.24427647058823532,
    0.28684470588235295,
    0.33063882352941182,
    0.37028352941176473,
    0.40439058823529417,
    0.43227882352941183,
    0.45577764705882357,
    0.47360352941176476,
    0.48674117647058823,
    0.49979882352941163,
], [
    0.10779898591549292,
    0.15870338028169012,
    0.24335419718309842,
    0.30154478873239432,
    0.31312512676056359,
    0.31187740845070405,
    0.30963605633802815,
    0.30475785915492964,
    0.30064743661971804,
    0.29648360563380305,
    0.28867476056338026,
    0.27758146478873252,
    0.27091515492957735,
    0.26409166197183093,
    0.25295690140845062,
    0.24406754929577457,
    0.24216214084507048,
    0.24517898591549292,
    0.2437064788732394,
    0.24752726760563384,
    0.25809814084507027,
    0.27048856338028177,
    0.2794646760563379,
    0.2856480563380282,
    0.28950569014084515,
    0.29394118309859157,
    0.29796377464788726,
    0.30271183098591542,
    0.3062855211267605,
    0.30746732394366194,
    0.30875188732394343,
    0.30856918309859155,
    0.31044997183098588,
    0.31218912676056354,
    0.31383464788732385,
    0.31724743661971833,
], [
    0.088915882352941178,
    0.11170882352941176,
    0.13155529411764705,
    0.13345352941176472,
    0.12773352941176472,
    0.12348058823529412,
    0.12199294117647061,
    0.11907411764705882,
    0.11792117647058822,
    0.11871352941176466,
    0.11512823529411763,
    0.10845,
    0.10843000000000001,
    0.11113294117647059,
    0.10788647058823528,
    0.10542588235294116,
    0.11212294117647059,
    0.13771529411764705,
    0.18127705882352937,
    0.22836529411764706,
    0.28692647058823539,
    0.35075411764705883,
    0.39709058823529408,
    0.42251705882352941,
    0.43389176470588225,
    0.43937470588235289,
    0.44075882352941176,
    0.44195411764705883,
    0.442395294117647,
    0.44206588235294109,
    0.4427305882352941,
    0.4424241176470588,
    0.44468470588235293,
    0.44592764705882354,
    0.44652235294117637,
    0.44930823529411767,
], [
    0.08701444444444445,
    0.10270333333333331,
    0.11151777777777777,
    0.10953777777777778,
    0.10569999999999999,
    0.10276222222222224,
    0.10133111111111109,
    0.097415555555555547,
    0.093923333333333345,
    0.090281111111111104,
    0.084862222222222214,
    0.078736666666666649,
    0.076061111111111107,
    0.073590000000000017,
    0.070440000000000003,
    0.069704444444444444,
    0.071597777777777788,
    0.07601444444444444,
    0.078996666666666673,
    0.092162222222222215,
    0.12827333333333332,
    0.20277777777777778,
    0.30198333333333338,
    0.40135111111111121,
    0.48075777777777773,
    0.53332888888888896,
    0.56130111111111125,
    0.57818000000000003,
    0.58851111111111121,
    0.5932211111111112,
    0.5978255555555555,
    0.60259555555555566,
    0.61115000000000008,
    0.61758111111111114,
    0.62303444444444445,
    0.62989222222222208,
], [
    0.070238571428571428,
    0.081116428571428589,
    0.089233095238095236,
    0.090286190476190478,
    0.089052857142857086,
    0.088346428571428548,
    0.089523571428571397,
    0.090568809523809496,
    0.09293809523809525,
    0.096935952380952373,
    0.10173238095238095,
    0.10764285714285717,
    0.12443142857142857,
    0.16565285714285716,
    0.22232071428571437,
    0.26490809523809533,
    0.29603785714285719,
    0.3389119047619048,
    0.3937452380952382,
    0.44306047619047628,
    0.46590380952380966,
    0.478242619047619,
    0.48273738095238095,
    0.48290047619047627,
    0.48206547619047607,
    0.48232547619047622,
    0.48180452380952365,
    0.48200666666666664,
    0.48249571428571431,
    0.48179785714285728,
    0.48414190476190488,
    0.48353404761904767,
    0.48836785714285708,
    0.49024928571428561,
    0.49035238095238093,
    0.49339000000000011,
]])
"""
Cluster means for *Otsu et al. (2018)*. This is a list of eight arrays, with
one for entry for each cluster. Each array is the mean of all spectral
distributions used to create the particular cluster, quantised with accordance
to ``OTSU_2018_SPECTRAL_SHAPE``.

References
----------
:cite:`Otsu2018`

OTSU_2018_MEANS : ndarray
"""

OTSU_2018_SELECTOR_ARRAY = np.array(
    [[1, 0.333444973048471, -3, -1], [0, 0.428556829741043, 1, -2],
     [1, 0.368343583792887, 5, 7], [0, 0.389059234962091, -5, -4],
     [0, 0.464102042665547, 2, 6], [0, 0.288243127874986, 0,
                                    -6], [1, 0.247072787814766, 3, 4]])
"""
Array describing how to choose the appropriate cluster given *CIE xy*
chromaticity coordinates.

OTSU_2018_SELECTOR_ARRAY : ndarray
"""

__all__ = [
    'OTSU_2018_SPECTRAL_SHAPE', 'OTSU_2018_BASIS_FUNCTIONS', 'OTSU_2018_MEANS',
    'OTSU_2018_SELECTOR_ARRAY'
]
