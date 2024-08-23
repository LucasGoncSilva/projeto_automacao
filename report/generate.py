from typing import Final


REPORT_MODEL = """<!DOCTYPE html><html lang="pt-br">

<head>
<title>Report</title><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><link rel="preconnect" href="https://fonts.googleapis.com">

<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Ubuntu:ital,wght@0,300;0,400;0,500;0,700;1,300;1,400;1,500;1,700&display=swap" rel="stylesheet">

    <style>
        * {{
            font-family: 'Ubuntu';
            margin: 0;
            padding: 0;
            text-align: center;
        }}

        body {{
            margin: 3rem;
        }}

        h2 {{
            margin-bottom: 3rem;
        }}

        section {{
            width: 100%;
            margin: 5rem auto;
        }}

        .display-none {{
            display: none !important;
        }}

        #dashboards-btns {{
            display: flex;
            justify-content: space-evenly;
            margin: auto;
            width: 60%;
        }}

        .dashboard-btn {{
            border: 2px solid #aaa;
            width: 9rem;
            height: fit-content;
            padding: 1rem;
            transition: 300ms;
        }}

        .dashboard-btn:hover {{
            cursor: pointer;
            border-color: #000;
        }}

        .dashboard-btn>svg {{
            aspect-ratio: 1/1;
            height: 8rem;
            width: 8rem;
            fill: #777;
            transition: 300ms;
        }}

        .dashboard-btn>svg:hover {{
            fill: #000;
        }}

        #general-charts>#general-charts-charts {{
            width: 100%;
            display: inline-flex;
            justify-content: space-evenly;
            margin-bottom: 5rem;
        }}

        #general-charts>#general-charts-metrics {{
            width: 100%;
            display: inline-flex;
            justify-content: space-evenly;
            margin-bottom: 5rem;
        }}

        #manual-vs-auto>#manual-vs-auto-data {{
            margin: 6rem auto;
            display: inline-flex;
            justify-content: space-evenly;
            width: 80%;
            font-weight: bold;
        }}

        #manual-vs-auto>#manual-vs-auto-data div:nth-child(1) {{
            color: #a00;
            border-color: #a00;
        }}

        #manual-vs-auto>#manual-vs-auto-data div:nth-child(2) {{
            color: #0a0;
            border-color: #0a0;
        }}

        #manual-vs-auto>#manual-vs-auto-data div:nth-child(3) {{
            color: #3c3caf;
            border-color: #3c3caf;
        }}

        #manual-vs-auto>#manual-vs-auto-data div:nth-child(4) {{
            color: #3c3caf;
            border-color: #3c3caf;
        }}

        #tests-details {{
            display: grid;
            grid-template-columns: auto auto;
            row-gap: 5rem;
        }}

        #tests-details > div {{
            width: 50rem;
            margin: auto;
        }}

        .individual-data {{
            aspect-ratio: 3/2;
            width: 10rem;
            padding: 1rem;
            border: 2px solid #ddd;
            border-radius: 20px;
            display: grid;
            grid-template-columns: auto;
            transition: 300ms;
        }}

        .individual-data h1 {{
            font-size: 2.5rem;
        }}

        .individual-data:hover {{
            border-color: #aaa;
        }}
    </style>
</head>

<body>
    <h1>Testes Automatizados</h1>
    <h2>Relatório de Execução</h2>


    <div id="dashboards-btns">

        <div class="dashboard-btn" data-dashboard="general-charts">
            <svg width="48" height="48" viewBox="0 0 12.7 12.7" version="1.1" id="svg1363"
                inkscape:version="1.2 (dc2aeda, 2022-05-15)" sodipodi:docname="general.svg"
                xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
                xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd" xmlns="http://www.w3.org/2000/svg"
                xmlns:svg="http://www.w3.org/2000/svg">
                <path id="path3593"
                    style="stroke:none;stroke-width:0.667571;stroke-linecap:butt;stroke-miterlimit:0;stroke-dasharray:none;paint-order:stroke fill markers"
                    d="m 6.2287419,1.0583333 a 5.2918786,5.2918786 0 0 0 -5.1704086,5.287103 5.2918786,5.2918786 0 0 0 0.00913,0.2386042 l 2.219801,-0.1532021 a 3.0674378,3.0674378 0 0 1 -0.00456,-0.085402 3.0674378,3.0674378 0 0 1 2.9440885,-3.0614347 z m 0.2529466,6.518e-4 -0.00261,2.2256683 a 3.0674378,3.0674378 0 0 1 2.938221,3.0607829 3.0674378,3.0674378 0 0 1 -0.234692,1.1767228 L 11.197704,8.4583219 A 5.2918786,5.2918786 0 0 0 11.641667,6.3454363 5.2918786,5.2918786 0 0 0 6.4816885,1.0589851 Z M 3.3029073,6.682481 1.0837583,6.8356831 A 5.2918786,5.2918786 0 0 0 6.3499998,11.637103 5.2918786,5.2918786 0 0 0 11.092747,8.687799 L 9.0743895,7.7503325 A 3.0674378,3.0674378 0 0 1 6.3499998,9.4127381 3.0674378,3.0674378 0 0 1 3.3029073,6.682481 Z" />
            </svg>
            <br>
            <span>Gráficos<br>Gerais</span>
        </div>

        <div class="dashboard-btn" data-dashboard="manual-vs-auto">
            <svg width="48" height="48" viewBox="0 0 12.7 12.7" version="1.1" id="svg3956" xml:space="preserve"
                inkscape:version="1.2 (dc2aeda, 2022-05-15)" sodipodi:docname="auto_vs_bot.svg"
                xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
                xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd" xmlns="http://www.w3.org/2000/svg"
                xmlns:svg="http://www.w3.org/2000/svg">
                <path id="path6771"
                    style="fill:#916f6f;stroke:none;stroke-width:0.0203461;stroke-miterlimit:0;stroke-dasharray:none;paint-order:stroke fill markers"
                    d="m 20.121242,17.353215 a 1.9004397,1.6724176 0 0 0 -1.90066,1.67225 1.9004397,1.6724176 0 0 0 1.90066,1.672766 1.9004397,1.6724176 0 0 0 1.900142,-1.672766 1.9004397,1.6724176 0 0 0 -1.900142,-1.67225 z m -1.033012,0.712618 a 0.39135537,0.39135537 0 0 1 0.391707,0.391191 0.39135537,0.39135537 0 0 1 -0.391707,0.39119 0.39135537,0.39135537 0 0 1 -0.391191,-0.39119 0.39135537,0.39135537 0 0 1 0.391191,-0.391191 z m 0.160713,1.83193 c 7.52e-4,-7e-5 0.0013,-9e-6 0.0021,0 0.0033,3.7e-5 0.0069,9.68e-4 0.01085,0.0026 0.461622,0.182694 1.294056,0.197422 1.784903,0 0.063,-0.02534 0.04802,0.155589 0,0.203605 -0.420728,0.420728 -1.364174,0.420728 -1.784903,0 -0.04431,-0.04431 -0.06029,-0.201818 -0.01292,-0.206189 z" />
                <path id="path4131"
                    style="stroke:none;stroke-width:0.585675;stroke-miterlimit:0;paint-order:stroke fill markers"
                    d="M 6.8982755,1.0583335 V 11.641666 H 7.0543162 V 1.0583335 Z M 9.2181607,2.0732071 A 0.24546354,0.24546354 0 0 0 8.9725187,2.3188493 0.24546354,0.24546354 0 0 0 9.1285593,2.5474244 V 4.4900082 A 2.9504519,3.4574989 0 0 0 7.2103567,3.6579947 V 4.992264 A 2.4756253,2.1785903 0 0 1 9.685673,7.1707374 2.4756253,2.1785903 0 0 1 7.2103567,9.3498202 V 10.573154 A 2.9504519,3.4574989 0 0 0 10.1605,7.1152698 2.9504519,3.4574989 0 0 0 9.3083717,4.6856685 V 2.5474244 A 0.24546354,0.24546354 0 0 0 9.4638028,2.3188493 0.24546354,0.24546354 0 0 0 9.2181607,2.0732071 Z M 6.5977754,2.1262365 C 5.0724135,2.1278131 3.6779917,2.4154957 2.5395001,3.6427564 3.6618358,4.267607 3.4214277,5.5393975 3.4251526,6.6953011 l 0.798489,0.2779473 C 4.2404021,4.7379074 5.4580765,4.890043 6.7422349,4.7722223 V 2.1311128 c -0.048254,-0.00303 -0.096464,-0.00494 -0.1444595,-0.00488 z m 0.1444595,2.777645 C 5.4887788,5.0190523 4.3003409,4.871411 4.2839855,7.0530974 L 3.5050015,6.7818548 c -1.69e-5,-0.00525 6.7e-6,-0.010592 0,-0.015848 -0.3392562,0.061508 -0.4627526,0.5019937 0.2090701,1.5488251 0.053517,0.083394 0.1947029,0.061822 0.3321958,-0.030477 0.4630156,1.3623005 1.5176765,2.2576761 2.6959675,2.2887981 V 8.8250117 C 6.3873088,8.8000799 6.0461161,8.6780831 5.8261058,8.4580725 5.7738394,8.4058066 5.754987,8.2200237 5.8108674,8.2148686 c 8.868e-4,-8.19e-5 0.00151,-1.05e-5 0.00244,0 0.00395,4.42e-5 0.00815,0.00121 0.0128,0.00305 0.2430977,0.096211 0.5734456,0.1525953 0.9161291,0.1651836 z m 0.4681218,0.2944048 v 3.1720134 c 0.3943966,0.00481 0.7956305,-0.04855 1.0916749,-0.1676218 0.07431,-0.029889 0.056641,0.1835207 0,0.2401562 C 8.0458362,8.6990304 7.625538,8.8223717 7.2103567,8.8140402 V 9.1437979 A 2.241606,1.9726495 0 0 0 9.4516121,7.1707374 2.241606,1.9726495 0 0 0 7.2103567,5.1982863 Z m 1.5969784,0.7375357 0.046324,0.1920032 c 0,0 -0.6333054,0.045106 -0.6333054,0.3638916 0,0.3187913 0.6333054,0.363282 0.6333054,0.363282 L 8.8073351,7.047002 c 0,0 -0.6169515,-0.1310914 -0.7710602,-0.4559312 -0.02628,-0.05539 -0.02628,-0.1439275 0,-0.1993175 C 8.1903836,6.0669133 8.8073351,5.935822 8.8073351,5.935822 Z M 5.6213024,6.0540716 C 5.8763293,6.0538422 6.0832218,6.2604616 6.083329,6.5154886 6.0832218,6.7705156 5.8763293,6.977135 5.6213024,6.9769056 5.3665136,6.9767983 5.1599926,6.7702775 5.1598854,6.5154886 5.1599926,6.2606997 5.3665136,6.0541789 5.6213024,6.0540716 Z" />
                <g aria-label="&lt;" id="text6697"
                    style="font-size:3.175px;font-family:Ubuntu;-inkscape-font-specification:Ubuntu;stroke-width:0.0264583;stroke-miterlimit:0;paint-order:stroke fill markers"
                    transform="matrix(0.47648067,0,0,0.66530224,14.48933,11.665395)">
                    <path
                        d="m 13.616525,10.197187 c 0,0.406241 1.127125,0.46355 1.127125,0.46355 l -0.08255,0.244475 c 0,0 -1.097395,-0.167076 -1.3716,-0.581025 -0.04676,-0.07058 -0.04676,-0.183415 0,-0.254 0.274205,-0.4139488 1.3716,-0.5810249 1.3716,-0.5810249 l 0.08255,0.244475 c 0,0 -1.127125,0.057308 -1.127125,0.4635499 z"
                        id="path6749" sodipodi:nodetypes="accaacca" />
                    <g aria-label="&lt;" id="g6769"
                        style="font-size:3.175px;font-family:Ubuntu;-inkscape-font-specification:Ubuntu;stroke-width:0.0264583;stroke-miterlimit:0;paint-order:stroke fill markers;fill:#aa0000"
                        transform="matrix(0.47648067,0,0,0.66530224,5.9441263,4.5296441)" />
            </svg>
            <br>
            <span>Manual vs<br>Automação</span>
        </div>

        <div class="dashboard-btn" data-dashboard="tests-details">
            <svg width="48" height="48" viewBox="0 0 12.7 12.7" version="1.1" id="svg7438"
                inkscape:version="1.2 (dc2aeda, 2022-05-15)" sodipodi:docname="details.svg"
                xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
                xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd" xmlns="http://www.w3.org/2000/svg"
                xmlns:svg="http://www.w3.org/2000/svg">
                <path id="path7561" style="stroke-width:0.0264583;stroke-miterlimit:0;paint-order:stroke fill markers"
                    d="m 3.9000665,1.9175475 a 0.30673599,0.30673599 0 0 0 -0.306958,0.3064413 0.30673599,0.30673599 0 0 0 0.306958,0.306958 0.30673599,0.30673599 0 0 0 0.306958,-0.306958 0.30673599,0.30673599 0 0 0 -0.306958,-0.3064413 z M 4.5894301,2.3883198 A 0.22143181,0.22143181 0 0 0 4.368255,2.609495 0.22143181,0.22143181 0 0 0 4.5894301,2.8311869 0.22143181,0.22143181 0 0 0 4.811122,2.609495 0.22143181,0.22143181 0 0 0 4.5894301,2.3883198 Z M 2.9456028,3.5556905 c -0.073992,0.00375 -0.1322917,0.065085 -0.1322917,0.1400431 0,0.077376 0.06215,0.1395264 0.1395264,0.1395264 H 3.2396417 V 6.4247659 A 1.9470184,1.9470184 0 0 0 2.3099827,8.0830627 1.9470184,1.9470184 0 0 0 4.2571506,10.030231 1.9470184,1.9470184 0 0 0 6.2043186,8.0830627 1.9470184,1.9470184 0 0 0 5.2741428,6.4226989 V 3.83526 h 0.287321 c 0.077376,0 0.1395263,-0.06215 0.1395263,-0.1395264 0,-0.077377 -0.06215,-0.1400431 -0.1395263,-0.1400431 H 2.9528375 c -0.00242,0 -0.00485,-1.21e-4 -0.00723,0 z M 3.5517673,3.83526 H 4.9625339 V 6.6061502 A 1.6587206,1.6587206 0 0 1 5.9211318,8.1094176 1.6587206,1.6587206 0 0 1 4.2623183,9.7682311 1.6587206,1.6587206 0 0 1 2.6035048,8.1094176 1.6587206,1.6587206 0 0 1 3.5517673,6.6108011 Z m 4.0013062,0.1834513 a 0.18861081,0.18861081 0 0 0 -0.188619,0.188619 0.18861081,0.18861081 0 0 0 0.188619,0.1886189 0.18861081,0.18861081 0 0 0 0.188619,-0.1886189 0.18861081,0.18861081 0 0 0 -0.188619,-0.188619 z m 0.787032,0.1596802 A 0.12906322,0.12906322 0 0 0 8.2114312,4.3075825 0.12906322,0.12906322 0 0 0 8.3401055,4.4367736 0.12906322,0.12906322 0 0 0 8.4692966,4.3075825 0.12906322,0.12906322 0 0 0 8.3401055,4.1783915 Z M 7.8951715,4.4155863 A 0.11076764,0.11076764 0 0 0 7.7840671,4.5261738 0.11076764,0.11076764 0 0 0 7.8951715,4.6372782 0.11076764,0.11076764 0 0 0 8.005759,4.5261738 0.11076764,0.11076764 0 0 0 7.8951715,4.4155863 Z M 6.8730116,5.1416401 c -0.072759,0.00366 -0.1302246,0.063241 -0.1302246,0.1369426 0,0.076079 0.061381,0.1374593 0.1374593,0.1374593 H 7.3587701 V 7.9466369 C 6.4413066,8.9843111 4.9930212,10.780572 5.9655735,10.780572 c 3.8845392,0 0.2332355,0.0042 4.1015585,0 0.972552,-0.0011 -0.4757333,-1.797126 -1.3931967,-2.8344519 V 5.416042 h 0.4785234 c 0.07608,0 0.13746,-0.061381 0.13746,-0.1374593 0,-0.076079 -0.06138,-0.1369426 -0.13746,-0.1369426 H 6.8802463 c -0.00238,0 -0.00489,-1.182e-4 -0.00723,0 z M 7.6605605,5.416042 h 0.7115844 v 2.6494507 c 0.7067538,0.7802814 2.1564471,2.4878033 1.3027628,2.4887373 -3.1283397,0.0034 -0.175657,0 -3.3171101,0 -0.8536165,0 0.5959455,-1.7075715 1.3027629,-2.4882206 z M 3.8137668,7.5600972 C 3.5136136,7.5674172 3.0768827,7.7081183 2.9032281,7.7678364 A 1.3783855,1.3783855 0 0 0 2.8701551,8.0660094 1.3783855,1.3783855 0 0 0 4.2488823,9.4447366 1.3783855,1.3783855 0 0 0 5.6270928,8.0660094 1.3783855,1.3783855 0 0 0 5.6172728,7.9032287 C 5.4279058,7.9536057 5.1593239,8.0125658 4.9883706,7.9957297 4.5999097,7.9574727 4.289066,7.5949842 3.900065,7.5626812 c -0.022876,-0.0019 -0.047035,-0.00284 -0.072347,-0.00258 -0.00469,4.82e-5 -0.00919,-1.162e-4 -0.013953,0 z M 3.4530653,7.9145975 A 0.30673599,0.30673599 0 0 1 3.7595066,8.2210387 0.30673599,0.30673599 0 0 1 3.4530653,8.5279967 0.30673599,0.30673599 0 0 1 3.1461073,8.2210387 0.30673599,0.30673599 0 0 1 3.4530653,7.9145975 Z M 4.142429,8.3853698 A 0.22143181,0.22143181 0 0 1 4.3636041,8.6065449 0.22143181,0.22143181 0 0 1 4.142429,8.8282368 0.22143181,0.22143181 0 0 1 3.9207371,8.6065449 0.22143181,0.22143181 0 0 1 4.142429,8.3853698 Z m 3.5222656,0.5710246 c -0.1374187,0.00441 -0.3102731,0.043154 -0.4578532,0.083716 -0.4928911,0.6090301 -0.944268,1.2965616 -0.469222,1.2965616 2.4223503,0 0.145227,0.0026 2.5574663,0 0.426962,-4.67e-4 0.105864,-0.5560094 -0.3214271,-1.1105265 -0.1369119,0.03921 -0.2914347,0.072606 -0.4004923,0.064596 C 8.2754654,9.2688745 8.0391117,8.983874 7.7416925,8.958462 c -0.018047,-0.00154 -0.03687,-0.00222 -0.056844,-0.00207 -0.00438,3.37e-5 -0.00897,-1.089e-4 -0.013436,0 -0.00216,5.27e-5 -0.00454,-7.01e-5 -0.00672,0 z M 7.4915785,9.4473205 a 0.18861081,0.18861081 0 0 1 0.188619,0.1886189 0.18861081,0.18861081 0 0 1 -0.188619,0.188619 0.18861081,0.18861081 0 0 1 -0.188619,-0.188619 0.18861081,0.18861081 0 0 1 0.188619,-0.1886189 z M 8.2791274,9.6070006 A 0.12906322,0.12906322 0 0 1 8.4078017,9.7361917 0.12906322,0.12906322 0 0 1 8.2791274,9.8653828 0.12906322,0.12906322 0 0 1 8.1499363,9.7361917 0.12906322,0.12906322 0 0 1 8.2791274,9.6070006 Z M 7.8336765,9.8441955 A 0.11076764,0.11076764 0 0 1 7.9447808,9.9552998 0.11076764,0.11076764 0 0 1 7.8336765,10.065887 0.11076764,0.11076764 0 0 1 7.7230889,9.9552998 0.11076764,0.11076764 0 0 1 7.8336765,9.8441955 Z" />
            </svg>
            <br>
            <span>Detalhes<br>dos Testes</span>
        </div>

    </div>


    <section id="general-charts">
        <div id="general-charts-charts">
            <div style="height: 300px; width: 300px;">
                <h3>Tipos de Testes</h3>
                <canvas id="types"></canvas>
            </div>

            <div style="height: 300px; width: 300px;">
                <h3>Mediana da Duração de Casos: 6s</h3>
                <canvas id="under-over-5s"></canvas>
            </div>

            <div style="height: 300px; width: 300px;">
                <h3>System_A vs System_B</h3>
                <canvas id="cases-system_a-vs-system_b"></canvas>
            </div>

            <div style="height: 300px; width: 300px;">
                <h3>Mediana da Qtd. de Casos (4)</h3>
                <canvas id="cases-per-module"></canvas>
            </div>
        </div>

        <div id="general-charts-metrics">
            <div style="height: 600px; width: 45%;">
                <h3>Métricas</h3>

                <div style="display: grid; grid-template-columns: auto auto auto; padding: 5rem; height: 80%;">
                    <div class="individual-data">
                        <span>Total de Casos</span>
                        <h1>{TOTAL_CASES}</h1>
                    </div>
                    <div class="individual-data">
                        <span>Total de Cenários</span>
                        <h1>{TOTAL_SCENARIOS}</h1>
                    </div>
                    <div class="individual-data">
                        <span>Cenários Ignorados</span>
                        <h1>{TOTAL_SKIPPED}</h1>
                    </div>
                </div>
            </div>
        
            <div style="height: 600px; width: 45%;">
                <h3>Médias Gerais Aproximadas</h3>

                <div style="display: grid; grid-template-columns: auto auto auto; padding: 5rem; height: 80%;">
                    <div class="individual-data">
                        <span>Caso (s)</span>
                        <h1>{AVG_CASES}</h1>
                    </div>
                    <div class="individual-data">
                        <span>Caso WEB (s)</span>
                        <h1>{AVG_CASES_WEB}</h1>
                    </div>
                    <div class="individual-data">
                        <span>Caso API (s)</span>
                        <h1>{AVG_CASES_API}</h1>
                    </div>

                    <div class="individual-data">
                        <span>Cenário (s)</span>
                        <h1>{AVG_SCENARIOS}</h1>
                    </div>
                    <div class="individual-data">
                        <span>Cenário WEB (s)</span>
                        <h1>{AVG_SCENARIOS_WEB}</h1>
                    </div>
                    <div class="individual-data">
                        <span>Cenário API (s)</span>
                        <h1>{AVG_SCENARIOS_API}</h1>
                    </div>
                </div>
            </div>
        </div>
    </section>


    
    <section id="manual-vs-auto">
        <div style="height: 600px; width: 90%; margin: auto;">
            <h3>Comparação do Tempo de Execução por Teste (Manual vs Automatizado)</h3>
            <canvas id="automation-vs-manual-1"></canvas>
        </div>

        <br><br><br><br><br>

        <div style="height: 600px; width: 90%; margin: auto;">
            <h3>Tempo Total Acumulado</h3>
            <canvas id="automation-vs-manual-2"></canvas>
        </div>

        <br><br><br><br><br>

        <div id="manual-vs-auto-data">
            <div class="individual-data">
                <span>Acumulado Manual</span>
                <h1>{TOTAL_ACC_MANUAL}h</h1>
            </div>

            <div class="individual-data">
                <span>Acumulado Automatizado</span>
                <h1>{TOTAL_ACC_AUTO}s</h1>
            </div>

            <div class="individual-data">
                <span>Acumulado Paralelo</span>
                <h1>{TOTAL_ACC_PARALLEL}s</h1>
            </div>

            <div class="individual-data">
                <span>Eficiência de</span>
                <h1>{EFFICIENCY}x</h1>
            </div>
        </div>
    </section>



    <section id="tests-details">
        <div style="height: 600px">
            <h3>Tempo de Execução por Caso</h3>
            <canvas id="methods-duration"></canvas>
        </div>

        <div style="height: 600px">
            <h3>Ocorrências de Cenários p/ Qntd.</h3>
            <canvas id="methods-occurrences"></canvas>
        </div>

        <div style="height: 600px">
            <h3>Tempo de Execução | Quantidade de Cenários</h3>
            <canvas id="execution-method"></canvas>
        </div>

        <div style="height: fit-content">
            <h3>Média de Execução Geral (s)</h3>
            <canvas id="execution-cases"></canvas>
        </div>

        <div style="height: fit-content">
            <h3>Média de Execução WEB (s)</h3>
            <canvas id="execution-cases-web"></canvas>
        </div>

        <div style="height: fit-content">
            <h3>Média de Execução API (s)</h3>
            <canvas id="execution-cases-api"></canvas>
        </div>
    </section>

    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

    <script>
        document.querySelectorAll('section').forEach(function (elem) {{
            elem.classList.add('display-none')
        }});

        document.querySelectorAll('.dashboard-btn').forEach(function (btn) {{
            const section = btn.dataset.dashboard;

            btn.addEventListener('click', function () {{
                document.querySelectorAll('section').forEach(function (sect) {{
                    sect.classList.add('display-none')
                }});

                document.getElementById(section).classList.remove('display-none')
            }})
        }});


        const types = document.getElementById('types');
        const underOver5Sec = document.getElementById('under-over-5s');
        const casesSystemAVsSystemB = document.getElementById('cases-system_a-vs-system_b');
        const median = document.getElementById('cases-per-module');
        
        const autoVsManual1 = document.getElementById('automation-vs-manual-1');
        const autoVsManual2 = document.getElementById('automation-vs-manual-2');

        const executionMethod = document.getElementById('execution-method');
        const methodsDuration = document.getElementById('methods-duration');
        const methodsOccurrences = document.getElementById('methods-occurrences');
        const executionCases = document.getElementById('execution-cases');
        const executionCasesAPI = document.getElementById('execution-cases-api');
        const executionCasesWEB = document.getElementById('execution-cases-web');

        
        new Chart(types, {{
            type: 'doughnut',
            data: {{
                labels: ["WEB", "API"],
                datasets: [
                    {{
                        backgroundColor: ["{COLOR_WEB}77", "{COLOR_API}77"],
                        borderColor: ["{COLOR_WEB}", "{COLOR_API}"],
                        data: {DATA_RESOURCE_1}
                    }}
                ]
            }},
        }});

        new Chart(underOver5Sec, {{
            type: 'doughnut',
            data: {{
                labels: ["Abaixo", "Acima"],
                datasets: [
                    {{
                        backgroundColor: ["{COLOR1}77", "{COLOR2}77"],
                        borderColor: ["{COLOR1}", "{COLOR2}"],
                        data: {DATA_RESOURCE_2}
                    }}
                ]
            }},
        }});

        new Chart(casesSystemAVsSystemB, {{
            type: 'doughnut',
            data: {{
                labels: ["System_A", "System_B"],
                datasets: [
                    {{
                        backgroundColor: ["{COLOR_System_A}77", "{COLOR_System_B}77"],
                        borderColor: ["{COLOR_System_A}", "{COLOR_System_B}"],
                        data: {DATA_RESOURCE_3}
                    }}
                ]
            }},
        }});

        new Chart(median, {{
            type: 'doughnut',
            data: {{
                labels: ["Abaixo", "Igual", "Acima"],
                datasets: [
                    {{
                        backgroundColor: ["{COLOR3}77", "{COLOR4}77", "{COLOR5}77"],
                        borderColor: ["{COLOR3}", "{COLOR4}", "{COLOR5}"],
                        data: {DATA_RESOURCE_4}
                    }}
                ]
            }},
        }});

        // 
        // 
        // 

        new Chart(autoVsManual1, {{
            type: 'line',
            data: {{
                labels: {TESTCASES},
                datasets: [
                    {{
                        label: 'Teste Automatizado',
                        data: {AUTO_DURATION},
                        borderColor: '{COLOR_System_A}',
                        backgroundColor: '#0000',
                        fill: true
                    }},
                    {{
                        label: 'Teste Manual',
                        data: {MANUAL_DURATION},
                        borderColor: '{COLOR_System_B}',
                        backgroundColor: '#0000',
                        fill: true
                    }},
                ]
            }},
            options: {{
                maintainAspectRatio: false,
                responsive: true,
                plugins: {{
                    title: {{
                        display: false,
                    }},
                    // tooltip: {{
                    //     mode: 'index'
                    // }},
                }},
                interaction: {{
                    mode: 'nearest',
                    axis: 'x',
                    intersect: false
                }},
                scales: {{
                    x: {{
                        title: {{
                            display: true,
                            text: 'Casos de Teste'
                        }}
                    }},
                    y: {{
                        stacked: false,
                        title: {{
                            display: true,
                            text: 'Tempo de Execução (s)',
                        }},
                        type: 'logarithmic',
                    }}
                }}
            }}
        }});

        new Chart(autoVsManual2, {{
            type: 'line',
            data: {{
                labels: {TESTCASES},
                datasets: [
                    {{
                        label: 'Teste Automatizado',
                        data: {AUTO_DURATION},
                        borderColor: '{COLOR_System_A}44',
                        backgroundColor: '#0000',
                        fill: true
                    }},
                    {{
                        label: 'Teste Manual',
                        data: {MANUAL_DURATION},
                        borderColor: '{COLOR_System_B}44',
                        backgroundColor: '#0000',
                        fill: true
                    }},
                    {{
                        label: 'Acumulado Automatizado Paralelo',
                        data: {PARALLEL_DURATION_ACCUMULATED},
                        borderColor: '#4717f6',
                        backgroundColor: '#0000',
                        fill: true
                    }},
                    {{
                        label: 'Acumulado Automatizado',
                        data: {AUTO_DURATION_ACCUMULATED},
                        borderColor: '#34eb5e',
                        backgroundColor: '#0000',
                        fill: true
                    }},
                    {{
                        label: 'Acumulado Manual',
                        data: {MANUAL_DURATION_ACCUMULATED},
                        borderColor: '#c70404',
                        backgroundColor: '#0000',
                        fill: true
                    }},
                ]
            }},
            options: {{
                maintainAspectRatio: false,
                responsive: true,
                plugins: {{
                    title: {{
                        display: false,
                    }},
                    // tooltip: {{
                    //     mode: 'index'
                    // }},
                }},
                interaction: {{
                    mode: 'nearest',
                    axis: 'x',
                    intersect: false
                }},
                scales: {{
                    x: {{
                        title: {{
                            display: true,
                            text: 'Casos de Teste'
                        }}
                    }},
                    y: {{
                        stacked: false,
                        title: {{
                            display: true,
                            text: 'Tempo de Execução (s)',
                        }},
                        type: 'logarithmic',
                    }}
                }}
            }}
        }});
        
        // 
        // 
        // 

        new Chart(methodsDuration, {{
            type: 'bar',
            data: {{
                labels: {CASE_NAMES},
                datasets: [
                    {{
                        label: "Duração (s)",
                        backgroundColor: '{COLOR_System_A}77',
                        borderWidth: 2,
                        borderColor: '{COLOR_System_A}',
                        data: {EXEC_TIME}
                    }}
                ]
            }},
            options: {{
                scales: {{
                    x: {{
                        title: {{
                            display: true,
                            text: 'Duração (s)'
                        }}
                    }},
                    y: {{
                        title: {{
                            display: true,
                            text: 'Nome do Caso de Teste'
                        }}
                    }}
                }},
                legend: {{ display: false }},
                indexAxis: 'y',
                label: {{ display: false }},
                maintainAspectRatio: false,
            }}
        }});

        new Chart(executionMethod, {{
            type: 'scatter',
            data: {{
                datasets: [
                    {{
                        label: 'WEB',
                        data: [{WEB}],
                        borderColor: '{COLOR_WEB}',
                        backgroundColor: '{COLOR_WEB}77',
                        pointRadius: 5,
                    }}, {{
                        label: 'API',
                        data: [{API}],
                        borderColor: '{COLOR_API}',
                        backgroundColor: '{COLOR_API}77',
                        pointRadius: 5,
                    }},
                ]
            }},
            options: {{
                scales: {{
                    x: {{
                        title: {{
                            display: true,
                            text: 'Duração (s)'
                        }}
                    }},
                    y: {{
                        title: {{
                            display: true,
                            text: 'Cenários por Caso'
                        }}
                    }}
                }},
                responsive: true,
                plugins: {{
                    legend: {{
                        position: 'top',
                    }},
                    title: {{
                        display: false,
                    }},
                }},
                maintainAspectRatio: false,
            }},
        }});

        // 
        // 
        // 

        new Chart(methodsOccurrences, {{
            type: 'bar',
            data: {{
                labels: {SCENARIOS_COUNT_VALUES},
                datasets: [
                    {{
                        label: "Quantidade",
                        backgroundColor: "{COLOR_System_B}77",
                        borderWidth: 2,
                        borderColor: "{COLOR_System_B}",
                        data: {SCENARIOS_COUNT_OCCURRENCES}
                    }}
                ]
            }},
            options: {{
                indexAxis: 'y',
                scales: {{
                    x: {{
                        title: {{
                            display: true,
                            text: 'Ocorrências'
                        }}
                    }},
                    y: {{
                        title: {{
                            display: true,
                            text: 'Cenários por Caso'
                        }}
                    }}
                }},
                legend: {{ display: false }},
                title: {{
                    display: false,
                }},
                maintainAspectRatio: false,
            }}
        }});

        //
        //
        //

        new Chart(executionCases, {{
            type: 'bar',
            data: {{
                labels: ['Top 1', 'Top 2', 'Top 3', 'Top 4', 'Top 5', 'Top -5', 'Top -4', 'Top -3', 'Top -2', 'Top -1'],
                datasets: [{{
                    label: "10 Mais Curtos",
                    type: "line",
                    borderColor: "#34eb5e",
                    backgroundColor: "#0000",
                    data: {CHART1LOWER_MEDIAN},
                    fill: false
                }}, {{
                    label: "10 Mais Longos",
                    type: "line",
                    borderColor: "#c70404",
                    backgroundColor: "#0000",
                    data: {CHART1HIGHER_MEDIAN},
                    fill: false
                }}, {{
                    label: "Testes Individuais",
                    type: "bar",
                    borderWidth: 2,
                    backgroundColor: "#344a5377",
                    borderColor: "#344a53",
                    data: {CHART1BARS},
                }}
                ]
            }},
            options: {{
                scales: {{
                    y: {{
                        title: {{
                            display: true,
                            text: 'Duração (s)'
                        }}
                    }}
                }},
                title: {{
                    display: false,
                }},
                legend: {{ display: true }}
            }}
        }});

        new Chart(executionCasesWEB, {{
            type: 'bar',
            data: {{
                labels: ['Top 1', 'Top 2', 'Top 3', 'Top 4', 'Top 5', 'Top -5', 'Top -4', 'Top -3', 'Top -2', 'Top -1'],
                datasets: [{{
                    label: "10 Mais Curtos",
                    type: "line",
                    borderColor: "#34eb5e",
                    backgroundColor: "#0000",
                    data: {CHART2LOWER_MEDIAN},
                    fill: false
                }}, {{
                    label: "10 Mais Longos",
                    type: "line",
                    borderColor: "#c70404",
                    backgroundColor: "#0000",
                    data: {CHART2HIGHER_MEDIAN},
                    fill: false
                }}, {{
                    label: "Testes Individuais",
                    type: "bar",
                    borderWidth: 2,
                    backgroundColor: "{COLOR_WEB}77",
                    borderColor: "{COLOR_WEB}",
                    data: {CHART2BARS},
                }}
                ]
            }},
            options: {{
                scales: {{
                    y: {{
                        title: {{
                            display: true,
                            text: 'Duração (s)'
                        }}
                    }}
                }},
                title: {{
                    display: false,
                }},
                legend: {{ display: true }}
            }}
        }});

        new Chart(executionCasesAPI, {{
            type: 'bar',
            data: {{
                labels: ['Top 1', 'Top 2', 'Top 3', 'Top 4', 'Top 5', 'Top -5', 'Top -4', 'Top -3', 'Top -2', 'Top -1'],
                datasets: [{{
                    label: "10 Mais Curtos",
                    type: "line",
                    borderColor: "#34eb5e",
                    backgroundColor: "#0000",
                    data: {CHART3LOWER_MEDIAN},
                    fill: false
                }}, {{
                    label: "10 Mais Longos",
                    type: "line",
                    borderColor: "#c70404",
                    backgroundColor: "#0000",
                    data: {CHART3HIGHER_MEDIAN},
                    fill: false
                }}, {{
                    label: "Testes Individuais",
                    type: "bar",
                    borderWidth: 2,
                    backgroundColor: "{COLOR_API}77",
                    borderColor: "{COLOR_API}",
                    data: {CHART3BARS},
                }}
                ]
            }},
            options: {{
                scales: {{
                    y: {{
                        title: {{
                            display: true,
                            text: 'Duração (s)',
                        }}
                    }}
                }},
                title: {{
                    display: false,
                }},
                legend: {{ display: true }}
            }}
        }});
    </script>
</body>

</html>
"""


COLOR_WEB: Final[str] = "#ffc800"
COLOR_API: Final[str] = "#7a59f0"
COLOR_System_A: Final[str] = "#c12dcc"
COLOR_System_B: Final[str] = "#2192b5"
COLOR1: Final[str] = "#e14dec"
COLOR2: Final[str] = "#a10dac"
COLOR3: Final[str] = "#51c2e5"
COLOR4: Final[str] = "#2192b5"
COLOR5: Final[str] = "#016285"


try:
    with open("resource.csv", encoding="utf-8") as f:
        data: list[str] = f.readlines()
        cleaned: list[str] = []

        for i in data[1:]:
            cleaned.append(i.replace("\n", ""))

        output = "report.html"
except FileNotFoundError:
    with open("report/resource.csv", encoding="utf-8") as f:
        data: list[str] = f.readlines()
        cleaned: list[str] = []

        for i in data[1:]:
            cleaned.append(i.replace("\n", ""))

        output = "report/report.html"


name, _type, path, scenarios_count, exec_time, readable, manual_exec = (
    [],
    [],
    [],
    [],
    [],
    [],
    [],
)
for i in cleaned:
    dec = i.split(",")

    name.append(dec[0])
    _type.append(dec[1])
    path.append(dec[2])
    scenarios_count.append(dec[3])
    exec_time.append(dec[4])
    readable.append(dec[5])
    manual_exec.append(dec[6])

exec_time = list(map(float, exec_time))
scenarios_count = list(map(int, scenarios_count))
manual_exec = list(map(int, manual_exec))

# ----------------------------------
# ----------------------------------
# ----------------------------------
# ----------------------------------
# ----------------------------------


# ----------------------------------
# GRÁFICOS GERAIS
# ----------------------------------


# WEB vs API
web_count = len([i for i in _type if i == "WEB"])
api_count = len([i for i in _type if i == "API"])
DATA_RESOURCE_1 = [web_count, api_count]  # USE THIS

# Exec Time > 6 > Exec Time
less5sec = len([i for i in exec_time if i < 6])
more5sec = len([i for i in exec_time if i > 6])
DATA_RESOURCE_2 = [less5sec, more5sec]  # USE THIS

# System_A vs System_B
system_a_count = len(
    [
        i
        for i in zip(name, path)
        if i[1].startswith("test_web.test_system_a")
        or i[1].startswith("test_api.test_apisystem_a")
        or "APISystem_A" in i[0]
    ]
)
system_b_count = len(
    [
        i
        for i in zip(name, path)
        if i[1].startswith("test_web.test_system_b")
        or i[1].startswith("test_api.test_apisystem_b")
        or "APISystem_B" in i[0]
    ]
)
DATA_RESOURCE_3 = [system_a_count, system_b_count]  # USE THIS

# Cases >= 4 >= Cases
less4scenarios = len([i for i in scenarios_count if i < 4])
equal4scenarios = len([i for i in scenarios_count if i == 4])
more4scenarios = len([i for i in scenarios_count if i > 4])
DATA_RESOURCE_4 = [less4scenarios, equal4scenarios, more4scenarios]  # USE THIS

# Metrics
TOTAL_CASES = len(name)  # USE THIS
TOTAL_SCENARIOS = sum(scenarios_count)  # USE THIS
TOTAL_SKIPPED = 307  # USE THIS


# ----------------------------------
# MANUAL vs BOT
# ----------------------------------


# Automation vs Manual
auto_duration = []  # USE THIS
for i in exec_time:
    if i < 0.1:
        auto_duration.append(0.1)
    else:
        auto_duration.append(i)
base = list(zip(readable.copy(), manual_exec.copy(), auto_duration))
acc_manual = 0
acc_auto = 0
TESTCASES = []  # USE THIS
MANUAL_DURATION = []  # USE THIS
AUTO_DURATION = []  # USE THIS
MANUAL_DURATION_ACCUMULATED = []  # USE THIS
AUTO_DURATION_ACCUMULATED = []  # USE THIS
PARALLEL_DURATION_ACCUMULATED = []  # USE THIS
for i, e in enumerate(base, start=1):
    acc_manual += e[1]
    acc_auto += e[2]

    TESTCASES.append(e[0])
    MANUAL_DURATION.append(e[1])
    AUTO_DURATION.append(e[2])
    PARALLEL_DURATION_ACCUMULATED.append(441 / len(name) * i)

    MANUAL_DURATION_ACCUMULATED.append(acc_manual)
    AUTO_DURATION_ACCUMULATED.append(acc_auto)
TOTAL_ACC_MANUAL = round(MANUAL_DURATION_ACCUMULATED[-1] / 60 / 60)  # USE THIS
TOTAL_ACC_AUTO = round(AUTO_DURATION_ACCUMULATED[-1])  # USE THIS
TOTAL_ACC_PARALLEL = 441  # USE THIS
EFFICIENCY = round(
    MANUAL_DURATION_ACCUMULATED[-1] / TOTAL_ACC_PARALLEL
)  # USE THIS


# ----------------------------------
# TESTES CONTEMPLADOS
# ----------------------------------


# ----------------------------------
# DETALHES DOS TESTES
# ----------------------------------


# Exec Time List
sorted_data = list(sorted(list(zip(readable, exec_time)), key=lambda x: x[1]))
CASE_NAMES = [i[0] for i in sorted_data]  # USE THIS
EXEC_TIME = [i[1] for i in sorted_data]  # USE THIS


# Exec Time vs Scenarios
group = list(zip(_type, exec_time, scenarios_count))
# WEB
WEB = ",".join(
    [f"{{x: {i[1]}, y: {i[2]}}}" for i in group if i[0] == "WEB"]
)  # USE THIS
# API
API = ",".join([f"{{x: {i[1]}, y: {i[2]}}}" for i in group if i[0] == "API"])  # USE THIS


# Methods Count
a = list(set(scenarios_count))
b = [scenarios_count.count(i) for i in a]
inter = list(sorted(list(zip(a, b)), key=lambda x: x[1]))
SCENARIOS_COUNT_VALUES = [i[0] for i in inter]
SCENARIOS_COUNT_OCCURRENCES = [i[1] for i in inter]


# Avg Cases
AVG_CASES = sum(exec_time) / len(exec_time)  # USE THIS
# Avg Cases WEB
WEB_AVG_CASES = [i[1] for i in list(zip(_type, exec_time)) if i[0] == "WEB"]
AVG_CASES_WEB = sum(WEB_AVG_CASES) / len(WEB_AVG_CASES)  # USE THIS
# Avg Cases API
API_AVG_CASES = [i[1] for i in list(zip(_type, exec_time)) if i[0] == "API"]
AVG_CASES_API = sum(API_AVG_CASES) / len(API_AVG_CASES)  # USE THIS
# Avg Scenarios
AVG_SCENARIOS = sum(exec_time) / sum(scenarios_count)  # USE THIS
# Avg Scenarios WEB
AVG_SCENARIOS_WEB = sum(
    [i[1] for i in list(zip(_type, exec_time)) if i[0] == "WEB"]
) / sum(
    [i[1] for i in list(zip(_type, scenarios_count)) if i[0] == "WEB"]
)  # USE THIS
# Avg Scenarios API
AVG_SCENARIOS_API = sum(
    [i[1] for i in list(zip(_type, exec_time)) if i[0] == "API"]
) / sum([i[1] for i in list(zip(_type, scenarios_count)) if i[0] == "API"])  # USE THIS


# Mixed Chart 1
base = list(sorted(exec_time))
x = base[:10]
y = base[:-11:-1]
CHART1LOWER_MEDIAN = [sum(x) / 10] * 10  # USE THIS
CHART1HIGHER_MEDIAN = [sum(y) / 10] * 10  # USE THIS
CHART1LOWER1 = base[0]
CHART1LOWER2 = base[1]
CHART1LOWER3 = base[2]
CHART1LOWER4 = base[3]
CHART1LOWER5 = base[4]
CHART1HIGHER1 = base[-5]
CHART1HIGHER2 = base[-4]
CHART1HIGHER3 = base[-3]
CHART1HIGHER4 = base[-2]
CHART1HIGHER5 = base[-1]
CHART1BARS = [
    CHART1LOWER1,
    CHART1LOWER2,
    CHART1LOWER3,
    CHART1LOWER4,
    CHART1LOWER5,
    CHART1HIGHER1,
    CHART1HIGHER2,
    CHART1HIGHER3,
    CHART1HIGHER4,
    CHART1HIGHER5,
]  # USE THIS

# Mixed Chart 2
base = [
    i[1] for i in sorted(zip(_type, exec_time), key=lambda x: x[1]) if i[0] == "WEB"
]
x = base[:10]
y = base[:-11:-1]
CHART2LOWER_MEDIAN = [sum(x) / 10] * 10  # USE THIS
CHART2HIGHER_MEDIAN = [sum(y) / 10] * 10  # USE THIS
CHART2LOWER1 = base[0]
CHART2LOWER2 = base[1]
CHART2LOWER3 = base[2]
CHART2LOWER4 = base[3]
CHART2LOWER5 = base[4]
CHART2HIGHER1 = base[-5]
CHART2HIGHER2 = base[-4]
CHART2HIGHER3 = base[-3]
CHART2HIGHER4 = base[-2]
CHART2HIGHER5 = base[-1]
CHART2BARS = [
    CHART2LOWER1,
    CHART2LOWER2,
    CHART2LOWER3,
    CHART2LOWER4,
    CHART2LOWER5,
    CHART2HIGHER1,
    CHART2HIGHER2,
    CHART2HIGHER3,
    CHART2HIGHER4,
    CHART2HIGHER5,
]  # USE THIS

# Mixed Chart 3
base = [i[1] for i in sorted(zip(_type, exec_time), key=lambda x: x[1]) if i[0] == "API"]
x = base[:10]
y = base[:-11:-1]
CHART3LOWER_MEDIAN = [sum(x) / 10] * 10  # USE THIS
CHART3HIGHER_MEDIAN = [sum(y) / 10] * 10  # USE THIS
CHART3LOWER1 = base[0]
CHART3LOWER2 = base[1]
CHART3LOWER3 = base[2]
CHART3LOWER4 = base[3]
CHART3LOWER5 = base[4]
CHART3HIGHER1 = base[-5]
CHART3HIGHER2 = base[-4]
CHART3HIGHER3 = base[-3]
CHART3HIGHER4 = base[-2]
CHART3HIGHER5 = base[-1]
CHART3BARS = [
    CHART3LOWER1,
    CHART3LOWER2,
    CHART3LOWER3,
    CHART3LOWER4,
    CHART3LOWER5,
    CHART3HIGHER1,
    CHART3HIGHER2,
    CHART3HIGHER3,
    CHART3HIGHER4,
    CHART3HIGHER5,
]  # USE THIS


# ----------------------------------
# ----------------------------------
# ----------------------------------
# ----------------------------------
# ----------------------------------


with open(output, "w", encoding="utf-8") as f:
    f.write(
        REPORT_MODEL.format(
            DATA_RESOURCE_1=DATA_RESOURCE_1,
            DATA_RESOURCE_2=DATA_RESOURCE_2,
            DATA_RESOURCE_3=DATA_RESOURCE_3,
            DATA_RESOURCE_4=DATA_RESOURCE_4,
            TOTAL_CASES=TOTAL_CASES,
            TOTAL_SCENARIOS=TOTAL_SCENARIOS,
            TOTAL_SKIPPED=TOTAL_SKIPPED,
            TESTCASES=TESTCASES,
            AUTO_DURATION=AUTO_DURATION,
            MANUAL_DURATION=MANUAL_DURATION,
            MANUAL_DURATION_ACCUMULATED=MANUAL_DURATION_ACCUMULATED,
            AUTO_DURATION_ACCUMULATED=AUTO_DURATION_ACCUMULATED,
            PARALLEL_DURATION_ACCUMULATED=PARALLEL_DURATION_ACCUMULATED,
            TOTAL_ACC_MANUAL=TOTAL_ACC_MANUAL,
            TOTAL_ACC_AUTO=TOTAL_ACC_AUTO,
            TOTAL_ACC_PARALLEL=TOTAL_ACC_PARALLEL,
            EFFICIENCY=EFFICIENCY,
            CASE_NAMES=CASE_NAMES,
            EXEC_TIME=EXEC_TIME,
            WEB=WEB,
            API=API,
            SCENARIOS_COUNT_VALUES=SCENARIOS_COUNT_VALUES,
            SCENARIOS_COUNT_OCCURRENCES=SCENARIOS_COUNT_OCCURRENCES,
            AVG_CASES=round(AVG_CASES, 2),
            AVG_CASES_WEB=round(AVG_CASES_WEB, 2),
            AVG_CASES_API=round(AVG_CASES_API, 2),
            AVG_SCENARIOS=round(AVG_SCENARIOS, 2),
            AVG_SCENARIOS_WEB=round(AVG_SCENARIOS_WEB, 2),
            AVG_SCENARIOS_API=round(AVG_SCENARIOS_API, 2),
            CHART1LOWER_MEDIAN=CHART1LOWER_MEDIAN,
            CHART1HIGHER_MEDIAN=CHART1HIGHER_MEDIAN,
            CHART1BARS=CHART1BARS,
            CHART2LOWER_MEDIAN=CHART2LOWER_MEDIAN,
            CHART2HIGHER_MEDIAN=CHART2HIGHER_MEDIAN,
            CHART2BARS=CHART2BARS,
            CHART3LOWER_MEDIAN=CHART3LOWER_MEDIAN,
            CHART3HIGHER_MEDIAN=CHART3HIGHER_MEDIAN,
            CHART3BARS=CHART3BARS,
            COLOR_WEB=COLOR_WEB,
            COLOR_API=COLOR_API,
            COLOR_System_A=COLOR_System_A,
            COLOR_System_B=COLOR_System_B,
            COLOR1=COLOR1,
            COLOR2=COLOR2,
            COLOR3=COLOR3,
            COLOR4=COLOR4,
            COLOR5=COLOR5,
        ),
    )

