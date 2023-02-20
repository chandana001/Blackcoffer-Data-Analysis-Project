from django.shortcuts import render,HttpResponse
import pymysql
import json


# Create your views here.
def home(request):
    json_data=open('jsondata.json',encoding='utf-8').read()
    json_obj=json.loads(json_data)
    con=pymysql.connect(host='127.0.0.1',user='root',password='nevergiveup',db='sys')
    cursor=con.cursor()
    for item in json_obj:
        endyear=item.get('end_year')
        
        intensity=item.get('intensity')
        
        sector=item.get('sector')
        topic=item.get('topic')
        insight=item.get('insight')
        url=item.get('url')
        region=item.get('region')
        start_year=item.get('start_year')
        impact=item.get('impact')
        added=item.get('added')
        published=item.get('published')
        country=item.get('country')
        relevance=item.get('relevance')
        pestle=item.get('pestle')
        source=item.get('source')
        title=item.get('title')
        likelihood=item.get('likelihood')
        if intensity=='':
            intensity=9
        if likelihood=='':
            likelihood=9
        if relevance=='':
            relevance=9
        # print(endyear,intensity,sector,topic,insight,url,region,start_year,impact,added,published,country,relevance,pestle,source,title,likelihood)
        # cursor.execute('insert into blackcoffer1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(endyear,intensity,sector,topic,insight,url,region,start_year,impact,added,published,country,relevance,pestle,source,title,likelihood))
        # cursor.execute("insert into blackcoffer1 values('',2,'Energy','gas','Annual Energy Outlook','http://www.eia.gov/outlooks/aeo/pdf/0383(2017).pdf','Northern America','','','January, 20 2017 03:51:25','January, 09 2017 00:00:00','United States of America',2,'Industries','EIA','U.S. natural gas consumption is expected to increase during much of the projection period.',3);")
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where sector="Energy";')
    energy=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where sector="Environment";')
    environment=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where sector="Government";')
    government=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where sector="Aerospace & defence";')
    aero=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where sector="Manufacturing";')
    manufacturing=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where sector="Retail";')
    retail=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where sector="Financial services";')
    financial=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where sector="Support services";')
    support=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where sector="Healthcare";')
    health=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where sector="Information Technology";')
    information=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where sector="Food & agriculture";')
    food=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where sector="Automotive";')
    automotive=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where sector="Tourism & hospitality";')
    tourism=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where sector="Construction";')
    construction=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where sector="Security";')
    security=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where sector="Transport";')
    transport=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where sector="Water";')
    water=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where sector="Media & entertainment";')
    media=cursor.fetchone()[0]
    
    
    
    con.commit()
    
    context={
        'Energy':energy,
        'Environment':environment,
        'Government':government,
        'Aerospace & defence':aero,
        'Manufacturing':manufacturing,
        'Retail':retail,
        'Financial services':financial,
        'Support services':support,
        'Information Technology':information,
        'Healthcare':health,
        'Food & agriculture':food,
        'Automotive':automotive,
        'Tourism & hospitality':tourism,
        'Construction':construction,
        'Security':security,
        'Transport':transport,
        'Water':water,
        'Media & entertainment':media

    }
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="growth";')
    growth=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="robot";')
    robot=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="strategy";')
    strategy=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="economy";')
    economy=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="oil";')
    oil=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="gas";')
    gas=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="consumption";')
    consumption=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="market";')
    market=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="gdp";')
    gdp=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="war";')
    war=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="production";')
    production=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="export";')
    export=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="battery";')
    battery=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="biofuel";')
    biofuel=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="policy";')
    policy=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="economic";')
    economic=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="energy";')
    energie=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="food";')
    foodie=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="administration";')
    administration=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="unemployment";')
    unemployment=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="trade";')
    trade=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="demand";')
    demand=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="economic growth";')
    economicgrowth=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="industry";')
    industry=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="capital";')
    capital=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="worker";')
    worker=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="tension";')
    tension=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="terrorism";')
    terrorism=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="transport";')
    transport=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="peak oil";')
    peakoil=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="vehicle";')
    vehicle=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="tourist";')
    tourist=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="artificial intelligence";')
    artificialintelligence=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="climate";')
    climate=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="power";')
    power=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="crisis";')
    crisis=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="ice";')
    ice=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="population";')
    population=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="politics";')
    politics=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="business";')
    business=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="work";')
    work=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="coal";')
    coal=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="gamification";')
    gamification=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="finance";')
    finance=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="interest rate";')
    interestrate=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="risk";')
    risk=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="inflation";')
    inflation=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="asylum";')
    asylum=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="resource";')
    resource=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="plastic";')
    plastic=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="electricity";')
    electricity=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="bank";')
    bank=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="gasoline";')
    gasoline=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="car";')
    car=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="money";')
    money=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="technology";')
    technology=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="aquaculture";')
    aquaculture=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="city";')
    city=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="investment";')
    investment=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="revenue";')
    revenue=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="emission";')
    emission=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="cimate change";')
    climatechange=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="infrastructure";')
    infrastructure=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="government";')
    government=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="security";')
    security=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="software";')
    software=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="building";')
    building=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="transportation";')
    transportation=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="wealth";')
    wealth=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="clothing";')
    clothing=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="shortage";')
    shortage=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="debt";')
    debt=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="agriculture";')
    agriculture=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="tax";')
    tax=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="carbon";')
    carbon=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="brexit";')
    brexit=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="workforce";')
    workforce=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="change";')
    change=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="automaker";')
    automaker=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="nuclear";')
    nuclear=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="3D";')
    threed=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="water";')
    water=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="data";')
    data=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="fossil fuel";')
    fossilfuel=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="election";')
    election=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic like "greenhouse%";')
    information=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="information";')
    information=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="shale gas";')
    shalegas=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="factory";')
    factory=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="farm";')
    farm=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic like "communicat%";')
    communication=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="storm";')
    storm=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="consumer";')
    consumer=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="material";')
    material=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="Washington";')
    Washington=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="pollution";')
    pollution=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where topic="fracking";')
    fracking=cursor.fetchone()[0]
    con.commit()
    
    topic={
        "gas":gas,
        "oil":oil,
        "consumption":consumption,
        "market":market,
        "war":war,
        "production":production,
        "export":export,
        "battery":battery,
        "biofuel":biofuel,
        "policy":policy,
        "economy":economy,
        "strategy":strategy,
        "robot":robot,
        "growth":growth,
        "economic":economic,
        "energy":energie,
        "foodie":foodie,
        "administration":administration,
        "unemployment":unemployment,
        "trade":trade,
        "demand":demand,
        "economicgrowth":economicgrowth,
        "industry":industry,
        "capital":capital,
        "worker":worker,
        "tension":tension,
        "terrorism":terrorism,
        "transport":transport,
        "peakoil":peakoil,
        "vehicle":vehicle,
        "tourist":tourist,
        "artificialintelligence":artificialintelligence,
        "climate":climate,
        "power":power,
        'crisis':crisis,
        'ice':ice,
        'population':population,
        'politics':politics,
        'business':business,
        'work':work,
        'coal':coal,
        'gamification':gamification,
        "finance":finance,
        "interestrate":interestrate,
        "risk":risk,
        "inflation":inflation,
        "asylum":asylum,
        "resource":resource,
        "plastic":plastic,
        "electricity":electricity,
        "bank":bank,
        "gasoline":gasoline,
        "car":car,
        "money":money,
        "technology":technology,
        "aquaculture":aquaculture,
        "city":city,
        "investment":investment,
        "revenue":revenue,
        "emisson":emission,
        "climatechange":climatechange,
        "infrastructure":infrastructure,
        "government":government,
        "security":security,
        "software":software,
        "building":building,
        "transportation":transportation,
        "wealth":wealth,
        "clothing":clothing,
        "shortage":shortage,
        "debt":debt,
        "agriculture":agriculture,
        "tax":tax,
        "carbon":carbon,
        "brexit":brexit,
        "workforce":workforce,
        "change":change,
        "automaker":automaker,
        "nuclear":nuclear,
        "threeed":threed,
        "water":water,
        "data":data,
        "fossilfuel":fossilfuel,
        "election":election,
        "information":information,
        "shalegas":shalegas,
        "factory":factory,
        "farm":farm,
        "communication":communication,
        "storm":storm,
        "consumer":consumer,
        "material":material,
        "Washington":Washington,
        "pollution":pollution,
        "fracking":fracking



    }

    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where endyear=2027;')
    twentyseven=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where endyear=2018;')
    eighteen=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where endyear=2025;')
    twentyfive=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where endyear=2040;')
    fourty=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where endyear=2200;')
    zero=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where endyear=2019;')
    nineteen=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where endyear=2020;')
    twenty=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where endyear=2022;')
    twentytwo=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where endyear=2017;')
    seventeen=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where endyear=2024;')
    twentyfour=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where endyear=2021;')
    twentyone=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where endyear=2026;')
    twentysix=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where endyear=2030;')
    thirty=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where endyear=2046;')
    fourtysix=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where endyear=2126;')
    twentysix=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where endyear=2050;')
    fifty=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where endyear=2041;')
    fourtyone=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where endyear=2035;')
    thirtyfive=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where endyear=2016;')
    sixteen=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where endyear=2055;')
    fiftyfive=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where endyear=2028;')
    twentyeight=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where endyear=2036;')
    thirtysix=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where endyear=2060;')
    sixty=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where endyear=2034;')
    thirtyfour=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where endyear=2051;')
    fiftyone=cursor.fetchone()[0]
    
    endyear={
        "fiftyone":fiftyone,
        "thirtyfour":thirtyfour,
        "sixty":sixty,
        "thirtysix":thirtysix,
        "twentyeight":twentyeight,
        "fiftyfive":fiftyfive,
        "sixteen":sixteen,
        "thirtyfive":thirtyfive,
        "fourtyone":fourtyone,
        "fifty":fifty,
        "twentysix":twentysix,
        "twentyone":twentyone,
        "twentyfour":twentyfour,
        "seventeen":seventeen,
        "twentytwo":twentytwo,
        "twenty":twenty,
        "nineteen":nineteen,
        "zero":zero,
        "fourty":fourty,
        "twentyfive":twentyfive,
        "eighteen":eighteen,
        "twentyseven":twentyseven,


    }
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where country="United States of America";')
    usa=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where country="Mexico";')
    Mexico=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where country="Nigeria";')
    Nigeria=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where country="Lebanon";')
    Lebanon=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where country="Russia";')
    Russia=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where country="Saudi Arabia";')
    SaudiArabia=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where country="Angola";')
    Angola=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where country="Egypt";')
    Egypt=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where country="South Africa";')
    SouthAfrica=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where country="India";')
    India=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where country="Ukraine";')
    Ukraine=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where country="Azerbaijan";')
    Azerbaijan=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where country="China";')
    China=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where country="Colombia";')
    Colombia=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where country="Niger";')
    Niger=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where country="Libya";')
    Libya=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where country="Brazil";')
    Brazil=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where country="Mali";')
    Mali=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where country ="Indonesia";')
    Indonesia=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where country="Iraq";')
    Iraq=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where country="Iran";')
    Iran=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where country="South Sudan";')
    SouthSudan=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where country="Venezuela";')
    Venezuela=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where country="Burkina Faso";')
    BurkinaFaso=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where country="Germany";')
    Germany=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where country="United Kingdom";')
    UnitedKingdom=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where country="Kuwait";')
    Kuwait=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where country="Canada";')
    Canada=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where country="Argentina";')
    Argentina=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where country="Japan";')
    Japan=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where country="Austria";')
    Austria=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where country="Spain";')
    Spain=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where country="Estonia";')
    Estonia=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where country="Hungary";')
    Hungary=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where country="Australia";')
    Australia=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where country="Morocco";')
    Morocco=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where country="Greece";')
    Greece=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where country="Qatar";')
    Qatar=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where country="Oman";')
    Oman=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where country="Liberia";')
    Liberia=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where country="Denmark";')
    Denmark=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where country="Malaysia";')
    Malaysia=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where country="Jordan";')
    Jordan=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where country="Syria";')
    Syria=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where country="Ethiopia";')
    Ethiopia=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where country="Norway";')
    Norway=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where country="Ghana";')
    Ghana=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where country="Kazakhstan";')
    Kazakhstan=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where country="Pakistan";')
    Pakistan=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where country="Gabon";')
    Gabon=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where country="United Arab Emirates";')
    UAE=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where country="Algeria";')
    Algeria=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where country="Turkey";')
    Turkey=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where country="Cyprus";')
    Cyprus=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where country="Belize";')
    Belize=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where country="Poland";')
    Poland=cursor.fetchone()[0]

    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where region="Northern America";')
    NorthernAmerica=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where region="Central America";')
    CentralAmerica=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where region like "%Africa%";')
    Africa=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where region like "%Asia%";')
    Asia=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where region like "%Europe%";')
    Europe=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where region= "South America";')
    SouthAmerica=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where region like "%Oceania%";')
    Oceania=cursor.fetchone()[0]

    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="EIA";')
    EIA=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="sustainablebrands.com";')
    sustainablebrandscom=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="SBWire";')
    SBWire=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="CleanTechnica";')
    CleanTechnica=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="TRAC News";')
    TRACNews=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Vanguard News";')
    VanguardNews=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Avi Melamed";')
    AviMelamed=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="WSJ";')
    WSJ=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Abq";')
    Abq=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Reuters";')
    Reuters=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Star Tribune";')
    StarTribune=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="EV Obsession";')
    EVObsession=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="creamermedia";')
    creamermedia=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Resilience";')
    Resilience=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="TheNews.NG";')
    security=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="FashionNetwork.com";')
    FashionNetworkcom=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Bloomberg Business";')
    BloombergBusiness=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Yes Bank";')
    YesBank=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="EGYPS";')
    EGYPS=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="marketrealist";')
    marketrealist=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="PDQFX news";')
    PDQFXnews=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="therobotreport";')
    therobotreport=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="nextbigfuture";')
    nextbigfuture=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="World Bank";')
    WorldBank=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Zero Hedge";')
    ZeroHedge=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Rigzone";')
    Rigzone=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="International Business Times";')
    security=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="DOE EIA 2013 Energy Conference";')
    DOEEIA2013EnergyConference=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="AllAfrica";')
    AllAfrica=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Energy.gov Website";')
    EnergygovWebsite=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="AMERICAN COUNCIL ON SCIENCE AND HEALTH";')
    AMERICANCOUNCILONSCIENCEANDHEALTH=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="The Jakarta Post";')
    TheJakartaPost=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Wharton";')
    Wharton=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="African Arguments";')
    AfricanArguments=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Business Insider";')
    BusinessInsider=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Convenience Store Decisions";')
    ConvenienceStoreDecisions=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="The Next Web";')
    TheNextWeb=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Cii Radio";')
    CiiRadio=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Global Money Trends";')
    GlobalMoneyTrends=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Guardian Sustainable Business";')
    GuardianSustainableBusiness=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="OklahomaMinerals.com";')
    OklahomaMineralscom=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="4th Annual Congress and Expo on Biofuels and Bioenergy April 27-28 2017 Dubai UAE";')
    fourthAnnualCongressandExpoonBiofuelsandBioenergyApril27282017DubaiUAE=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="FX Empire";')
    FXEmpire=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Nexus Conference";')
    NexusConference=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Fews Net";')
    FewsNet=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Sputnik News";')
    SputnikNews=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="platts";')
    platts=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="CBO";')
    CBO=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="The Chirographer";')
    TheChirographer=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="THE LEAGUE OF WOMEN VOTERS® OF THE FAIRFAX AREA";')
    THELEAGUEOFWOMENVOTERSOFTHEFAIRFAXAREA=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Yahoo Finance Canada";')
    YahooFinanceCanada=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Gii Research";')
    GiiResearch=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="South Sudan News Agency";')
    SouthSudanNewsAgency=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Climate Change News";')
    ClimateChangeNews=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="the star online";')
    thestaronline=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="khorreports-palmoil";')
    khorreportspalmoil=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Canadian Biomass";')
    CanadianBiomass=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Informed Choice Chartered Financial Planners in Cranleigh";')
    InformedChoiceCharteredFinancialPlannersinCranleigh=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Guarini Center";')
    GuariniCenter=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="OMFIF";')
    OMFIF=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="South World";')
    SouthWorld=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="World Energy News";')
    WorldEnergyNews=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Slinking Toward Retirement";')
    SlinkingTowardRetirement=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="unian";')
    unian=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Scientific American";')
    ScientificAmerican=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Time";')
    Time=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Transport Environment";')
    TransportEnvironment=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Triple Pundit";')
    TriplePundit=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Transport Evolved";')
    TransportEvolved=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Fox Business";')
    FoxBusiness=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="The Independent";')
    TheIndependent=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Biofuels Digest";')
    BiofuelsDigest=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="IRENA newsroom";')
    IRENAnewsroom=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Nation of Change";')
    NationofChange=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Middle East Eye";')
    MiddleEastEye=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="IEA";')
    IEA=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Gas 2";')
    Gas2=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Peak Prosperity";')
    PeakProsperity=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Business Wire";')
    BusinessWire=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="RiskMap 2017";')
    RiskMap2017=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="MRC";')
    MRC=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Insurance Journal";')
    InsuranceJournal=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Wired UK";')
    WiredUK=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Technavio";')
    Technavio=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="News";')
    News=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Media Center";')
    MediaCenter=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="EY";')
    EY=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Tactical Investor";')
    TacticalInvestor=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Seeking Alpha";')
    SeekingAlpha=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="iMFdirect - The IMF Blog";')
    iMFdirectTheIMFBlog=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="oilprice.com";')
    oilpricecom=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Eurasia Group";')
    EurasiaGroup=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="NY Times";')
    NYTimes=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Imeche";')
    Imeche=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="University of Chicago";')
    UniversityofChicago=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Adam Curry";')
    AdamCurry=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="JD Supra";')
    JDSupra=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="UK Government";')
    UKGovernment=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Investopedia";')
    Investopedia=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Vox";')
    Vox=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="South China Morning Post";')
    SouthChinaMorningPost=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="OEM/Lube News";')
    OEMLubeNews=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="PR Newswire";')
    PRNewswire=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Future Market Insights";')
    FutureMarketInsights=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Manufacturing Operations Technology Viewpoints";')
    ManufacturingOperationsTechnologyViewpoints=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="CSIS";')
    CSIS=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Edge and Odds";')
    EdgeandOdds=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="maltawinds.com";')
    maltawindscom=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="iamericas";')
    iamericas=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="cpzulia";')
    cpzulia=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="farms";')
    farms=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Le·gal In·sur·rec·tion";')
    LegalInsurrection=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="IFT";')
    IFT=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="International Banker";')
    InternationalBanker=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="bankofcanada";')
    bankofcanada=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Koenig Investment Advisory";')
    KoenigInvestmentAdvisory=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Europa";')
    Europa=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Jachin Capital";')
    JachinCapital=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Wells Fargo";')
    WellsFargo=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="ethicalconsumer";')
    ethicalconsumer=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Citibank";')
    Citibank=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Cornell University";')
    CornellUniversity=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="arabellaadvisors";')
    arabellaadvisors=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Critical Threats";')
    CriticalThreats=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Fitch";')
    Fitch=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="prsync";')
    prsync=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Physics World";')
    PhysicsWorld=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Renewable Energy World";')
    RenewableEnergyWorld=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="BBC News Technology";')
    BBCNewsTechnology=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="edie.net";')
    edienet=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Russia Beyond The Headlines";')
    RussiaBeyondTheHeadlines=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Politico";')
    Politico=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Tech Times";')
    TechTimes=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Wood McKenzie";')
    WoodMcKenzie=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="3D Printing Progress";')
    threeDPrintingProgress=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="ihsmarkit";')
    ihsmarkit=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Gizmodo Australia";')
    GizmodoAustralia=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="The Nation";')
    TheNation=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Farms.com";')
    Farmscom=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="McKinsey & Company";')
    McKinseyCompany=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="The Guardian";')
    TheGuardian=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Resources for the Future";')
    ResourcesfortheFuture=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="satprnews";')
    satprnews=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="GreenBiz";')
    GreenBiz=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="CNBC";')
    CNBC=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Sydney Morning Herald";')
    CNBC=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="www.narendramodi.in";')
    wwwnarendramodiin=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="CNNMoney";')
    CNNMoney=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="EIU";')
    EIU=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Euromoney";')
    Euromoney=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="gasstrategies";')
    gasstrategies=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Cars.co.za";')
    Carscoza=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="europeanclimate";')
    europeanclimate=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Australian Government";')
    AustralianGovernment=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="TeleTrade";')
    TeleTrade=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Bloomberg New Energy Finance";')
    BloombergNewEnergyFinance=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="The Economist";')
    TheEconomist=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Phys Org";')
    PhysOrg=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="djsresearch";')
    djsresearch=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="nbk";')
    nbk=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Guardian";')
    Guardian=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="cargill";')
    cargill=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Worldly";')
    Worldly=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Utility Dive";')
    UtilityDive=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="newscientist";')
    newscientist=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="westpandi";')
    westpandi=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="IASTOPPERS";')
    IASTOPPERS=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="THISDAY LIVE";')
    THISDAYLIVE=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="veteranstoday";')
    veteranstoday=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="thespanisheconomy";')
    thespanisheconomy=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="biologicaldiversity";')
    biologicaldiversity=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="portfolioticker";')
    portfolioticker=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="MIT Technology Review";')
    MITTechnologyReview=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="FoodQualityNews.com";')
    FoodQualityNewscom=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="The Conversation";')
    TheConversation=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="World Bank Group";')
    WorldBankGroup=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="TheCable";')
    TheCable=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Future Earth";')
    FutureEarth=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Carbon Brief";')
    CarbonBrief=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Wikipedia";')
    Wikipedia=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="NWF";')
    NWF=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="USDA";')
    USDA=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="energyglobal";')
    energyglobal=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="IEA.org";')
    IEAorg=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="PwC";')
    PwC=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="metalprices";')
    metalprices=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="GE Reports";')
    GEReports=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Project Syndicate";')
    ProjectSyndicate=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Interior Design";')
    InteriorDesign=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="idc-community";')
    idccommunity=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Science Daily";')
    ScienceDaily=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="The Mainichi";')
    TheMainichi=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="economy";')
    economy=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Drill or drop?";')
    Drillordrop=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Huffington Post";')
    HuffingtonPost=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Lawfare";')
    Lawfare=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Futureseek Link Digest";')
    FutureseekLinkDigest=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Environmental Leader";')
    EnvironmentalLeader=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Business Standard";')
    BusinessStandard=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="ESPAS";')
    ESPAS=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Euler Hermes";')
    EulerHermes=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="amundi";')
    amundi=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="ebrd";')
    ebrd=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Drydock Magazine";')
    DrydockMagazine=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="BorneoPost Online";')
    BorneoPostOnline=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Finance Magnates";')
    FinanceMagnates=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="friday-thinking";')
    fridaythinking=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Newsweek";')
    Newsweek=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="ECFR";')
    ECFR=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="University of Latvia";')
    UniversityofLatvia=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Future Timeline";')
    FutureTimeline=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="allianzglobalinvestors";')
    allianzglobalinvestors=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="controleng";')
    controleng=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="inputsmonitor";')
    inputsmonitor=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Planetsave";')
    Planetsave=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="agriworldsa";')
    agriworldsa=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="globalmoneytrends";')
    globalmoneytrends=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Oxfam";')
    Oxfam=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Gartner";')
    Gartner=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="clientadvisoryservices";')
    clientadvisoryservices=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="IMF";')
    IMF=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Eco-Business.com";')
    EcoBusinesscom=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Channel News Asia";')
    ChannelNewsAsia=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="War on the Rocks";')
    WarontheRocks=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="biomassmagazine";')
    biomassmagazine=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Think Progress";')
    ThinkProgress=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="No 2 Nuclear Power";')
    No2NuclearPower=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="ogauthority";')
    ogauthority=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="IBEF";')
    IBEF=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Prospects for Development";')
    ProspectsforDevelopment=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Engineering News";')
    EngineeringNews=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="NDTV";')
    NDTV=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="African Development Bank";')
    AfricanDevelopmentBank=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Aljazeera.com";')
    Aljazeeracom=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="worldenergy";')
    worldenergy=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="cloudfront";')
    cloudfront=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Zawya";')
    Zawya=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="FAO";')
    FAO=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="VOA";')
    VOA=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Hospitality Trends";')
    HospitalityTrends=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="saltlakecityheadlines";')
    saltlakecityheadlines=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="The Ticker Tape";')
    TheTickerTape=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="The Globe and Mail";')
    TheGlobeandMail=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="AgWeb - The Home Page of Agriculture";')
    AgWebTheHomePageofAgriculture=cursor.fetchone()[0]
    
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="CAFrackFacts";')
    CAFrackFacts=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="murc";')
    murc=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Fast Co-Exist";')
    FastCoExist=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Cushman & Wakefield Blog";')
    CushmanWakefield=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Science News";')
    ScienceNews=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Quartz";')
    Quartz=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Total";')
    Total=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="globalizationpartners";')
    globalizationpartners=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Washington Post";')
    WashingtonPost=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Inside Climate News";')
    InsideClimateNews=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="polymerspaintcolourjournal";')
    polymerspaintcolourjournal=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="njc-cnm";')
    njccnm=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="IISS";')
    IISS=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="The Atlantic";')
    TheAtlantic=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Innovations Report";')
    InnovationsReport=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Nature";')
    Nature=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Cushman & Wakefield";')
    CushmanWakefield=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Maplecroft";')
    Maplecroft=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Predictive Analytics Times";')
    PredictiveAnalyticsTimes=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="McKinsey Quarterly";')
    McKinseyQuarterly=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Countries.com Global Content";')
    CountriescomGlobalContent=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="The Market Mogul";')
    TheMarketMogul=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="knomad";')
    knomad=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="UNESCO ";')
    UNESCO=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="GlobalMeatNews.com";')
    GlobalMeatNewscom=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Motor Magazine";')
    MotorMagazine=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="MENA-Forum";')
    MENAForum=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Blue and Green Tomorrow";')
    BlueandGreenTomorrow=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="valburyresearch";')
    valburyresearch=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="HBR";')
    HBR=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Nanotechnology Innovation";')
    NanotechnologyInnovation=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="oilvoice";')
    oilvoice=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="ecesr";')
    ecesr=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Freedonia";')
    Freedonia=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="ethicalmarkets";')
    ethicalmarkets=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Climate News Network";')
    ClimateNewsNetwork=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="OPEC";')
    OPEC=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="INSEAD Knowledge";')
    INSEADKnowledge=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="CIO";')
    CIO=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Institutional Investor";')
    InstitutionalInvestor=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Society of Motor Manufacturers and Traders (SMMT)";')
    SocietyofMotorManufacturersandTradersSMMT=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="worldculturepictorial";')
    worldculturepictorial=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="globalfueleconomy";')
    globalfueleconomy=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="LiveMint";')
    LiveMint=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="g7g20";')
    g7g20=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Mast";')
    Mast=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="ReadWrite";')
    ReadWrite=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="LNG";')
    LNG=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="European Central Bank";')
    EuropeanCentralBank=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Industrial Control Security";')
    IndustrialControlSecurity=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Verisk Maplecroft";')
    VeriskMaplecroft=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="ETEnergyworld.com";')
    ETEnergyworldcom=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="briandcolwell";')
    briandcolwell=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="DW.COM";')
    DWCOM=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Elsevier";')
    Elsevier=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="MAPI";')
    MAPI=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Days Of Year";')
    DaysOfYear=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Virgin Atlantic";')
    VirginAtlantic=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Government of Ireland";')
    GovernmentofIreland=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="The Engineer";')
    TheEngineer=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="ISA";')
    ISA=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Energy Tomorrow";')
    EnergyTomorrow=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Justmeans";')
    Justmeans=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Khaleej Times";')
    KhaleejTimes=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Innovaro";')
    Innovaro=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="FutureinFocus";')
    FutureinFocus=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="What\'s Next";')
    WhatsNext=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Stanford News";')
    StanfordNews=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Middle East Online";')
    MiddleEastOnline=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Neon Nettle";')
    NeonNettle=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Handelsblatt Global Edition";')
    HandelsblattGlobalEdition=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="EE News";')
    EENews=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Before It\'s News | Alternative News | UFO | Beyond Science | True News| Prophecy News | People Powered News";')
    before=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="aswm";')
    aswm=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Shenandoah";')
    Shenandoah=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Digitalist Magazine";')
    DigitalistMagazine=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="EPA";')
    EPA=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Azonano";')
    Azonano=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="National Geographic Society (blogs)";')
    NationalGeographicSocietyblogs=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="IER";')
    IER=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Ocean Acidification";')
    OceanAcidification=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Smart Grid Observer";')
    SmartGridObserver=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Freenewspos";')
    Freenewspos=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="AHDB";')
    AHDB=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="SlideShare";')
    SlideShare=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="VITA Technologies";')
    VITATechnologies=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Wall Street Daily";')
    WallStreetDaily=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Bearnobull";')
    Bearnobull=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="CCN: Financial Bitcoin & Cryptocurrency News";')
    CCNFinancialBitcoinCryptocurrencyNews=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="IRENA";')
    IRENA=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="International Monetary Fund (IMF)";')
    InternationalMonetaryFundIMF=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Arangkada Philippines";')
    ArangkadaPhilippines=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Global Information Inc";')
    GlobalInformationInc=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="ID TECH INDEX";')
    IDTECHINDEX=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="The Jamestown Foundation";')
    TheJamestownFoundation=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="savepassamaquoddybay";')
    savepassamaquoddybay=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="atradius";')
    atradius=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="dailyquiddity";')
    dailyquiddity=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="bankofengland";')
    bankofengland=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Futurity";')
    Futurity=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Business Green";')
    BusinessGreen=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="About Best Binary Options Strategy";')
    AboutBestBinaryOptionsStrategy=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="IHS Engineering 360";')
    IHSEngineering360=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="European Council";')
    EuropeanCouncil=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Activist Post";')
    ActivistPost=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Newsletter";')
    Newsletter=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="U.S. Environmental Protection Agency";')
    USEnvironmentalProtectionAgency=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Global Money Trends Magazine";')
    GlobalMoneyTrendsMagazine=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="CAJ News Africa";')
    CAJNewsAfrica=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Planetizen";')
    Planetizen=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="CDC";')
    CDC=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Strategy & Formerly Booz & Company";')
    StrategyFormerlyBoozCompany=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="PriceWaterhouseCoopers";')
    PriceWaterhouseCoopers=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="News.com";')
    Newscom=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Brookings Institute";')
    BrookingsInstitute=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Innovate UK";')
    InnovateUK=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="The Arab Gulf States Institute Washington";')
    TheArabGulfStatesInstituteWashington=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Embedded Computing Design";')
    EmbeddedComputingDesign=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="European Environment Agency";')
    EuropeanEnvironmentAgency=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Industry Week";')
    IndustryWeek=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Atlantic Council ";')
    AtlanticCouncil=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="U.K. Ministry of Defense";')
    UKMinistryofDefense=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Future in Focus";')
    FutureinFocus=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Australian Government Department of Defence";')
    AustralianGovernmentDepartmentofDefence=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="MIT Sloan Management Review";')
    MITSloanManagementReview=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Scania Group";')
    ScaniaGroup=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="watercanada";')
    watercanada=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Common Dreams";')
    CommonDreams=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="theicct";')
    theicct=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="nbp";')
    nbp=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Thomson Reuters ";')
    ThomsonReuters=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="University Chronicle";')
    UniversityChronicle=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="globalr2p";')
    globalr2p=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Robothub";')
    Robothub=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="New Security Beat";')
    NewSecurityBeat=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="betterenergy";')
    betterenergy=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Real Estate Professional";')
    RealEstateProfessional=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Mind Commerce";')
    MindCommerce=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Yahoo Finance";')
    YahooFinance=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Pickens Plan";')
    PickensPlan=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="RUSI";')
    RUSI=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Hardin Tibbs";')
    HardinTibbs=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="World Health";')
    WorldHealth=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="environmentalpeacebuilding";')
    environmentalpeacebuilding=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="greenerearthnews";')
    greenerearthnews=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="conferenceseries";')
    conferenceseries=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="dailytexanonline";')
    dailytexanonline=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="EPS News";')
    EPSNews=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="The American Prospect";')
    TheAmericanProspect=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Face2face Africa";')
    Face2faceAfrica=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Oil and Gas Journal";')
    OilandGasJournal=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="Infracircle";')
    Infracircle=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="uschamber";')
    uschamber=cursor.fetchone()[0]
    cursor.execute('select cast(sum(intensity)as unsigned) from blackcoffer1 where source="energy news cyprus";')
    energynewscyprus=cursor.fetchone()[0]
    
    source={
        "EIA":EIA,
        "sustainablebrandscom":sustainablebrandscom,
        "SBWire":SBWire,
        "CleanTechnica":CleanTechnica,
        "TRACNews":TRACNews,
        "VanguardNews":VanguardNews,
        "AviMelamed":AviMelamed,
        "WSJ":WSJ,
        "Abq":Abq,
        "Reuters":Reuters,
        "StarTribune":StarTribune,
        "EVObsession":EVObsession,
        "creamermedia":creamermedia,
        "Resilience":Resilience,
        "FashionNetworkcom":FashionNetworkcom,
        "BloombergBusiness":BloombergBusiness,
        "YesBank":YesBank,
        "EGYPS":EGYPS,
        "marketrealist":marketrealist,
        "PDQFXnews":PDQFXnews,
        "therobotreport":therobotreport,
        "nextbigfuture":nextbigfuture,
        "WorldBank":WorldBank,
        "ZeroHedge":ZeroHedge,
        "Rigzone":Rigzone,
        "DOEEIA2013EnergyConference":DOEEIA2013EnergyConference,
        "AllAfrica":AllAfrica,
        "AMERICANCOUNCILONSCIENCEANDHEALTH":AMERICANCOUNCILONSCIENCEANDHEALTH,
        "TheJakartaPost":TheJakartaPost,
        "Wharton":Wharton,
        "AfricanArguments":AfricanArguments,
        "BusinessInsider":BusinessInsider,

        "ConvenienceStoreDecisions":ConvenienceStoreDecisions,
        "TheNextWeb":TheNextWeb,
        "CiiRadio":CiiRadio,
        "GlobalMoneyTrends":GlobalMoneyTrends,
        "GuardianSustainableBusiness":GuardianSustainableBusiness,
        "OklahomaMineralscom":OklahomaMineralscom,
        "fourthAnnualCongressandExpoonBiofuelsandBioenergyApril27282017DubaiUAE":fourthAnnualCongressandExpoonBiofuelsandBioenergyApril27282017DubaiUAE,
        "FXEmpire":FXEmpire,
        "NexusConference":NexusConference,
        "FewsNet":FewsNet,
        "SputnikNews":SputnikNews,
        "platts":platts,
        "CBO":CBO,
        "TheChirographer":TheChirographer,
        "THELEAGUEOFWOMENVOTERSOFTHEFAIRFAXAREA":THELEAGUEOFWOMENVOTERSOFTHEFAIRFAXAREA,
        "YahooFinanceCanada":YahooFinanceCanada,
        "GiiResearch":GiiResearch,
        "SouthSudanNewsAgency":SouthSudanNewsAgency,
        "ClimateChangeNews":ClimateChangeNews,
        "thestaronline":thestaronline,
        "khorreportspalmoil":khorreportspalmoil,
        "CanadianBiomass":CanadianBiomass,
        "InformedChoiceCharteredFinancialPlannersinCranleigh":InformedChoiceCharteredFinancialPlannersinCranleigh,
        "GuariniCenter":GuariniCenter,
        "OMFIF":OMFIF,
        "SouthWorld":SouthWorld,
        "WorldEnergyNews":WorldEnergyNews,
        "SlinkingTowardRetirement":SlinkingTowardRetirement,
        "unian":unian,
        "ScientificAmerican":ScientificAmerican,
        "Time":Time,
        "TransportEnvironment":TransportEnvironment,
        "TriplePundit":TriplePundit,
        "TransportEvolved":TransportEvolved,
        "FoxBusiness":FoxBusiness,
        "TheIndependent":TheIndependent,
        "BiofuelsDigest":BiofuelsDigest,
        "IRENAnewsroom":IRENAnewsroom,
        "NationofChange":NationofChange,
        "MiddleEastEye":MiddleEastEye,
        "IEA":IEA,
        "Gas2":Gas2,
        "PeakProsperity":PeakProsperity,
        "BusinessWire":BusinessWire,
        "RiskMap2017":RiskMap2017,
        "MRC":MRC,
        "InsuranceJournal":InsuranceJournal,
        "WiredUK":WiredUK,
        "Technavio":Technavio,
        "News":News,
        "MediaCenter":MediaCenter,
         "EY":EY,
         "TacticalInvestor":TacticalInvestor,
         "SeekingAlpha":SeekingAlpha,
         "iMFdirectTheIMFBlog":iMFdirectTheIMFBlog,
         "oilpricecom":oilpricecom,
         "EurasiaGroup":EurasiaGroup,
         "NYTimes":NYTimes,
         "Imeche":Imeche,
        "UniversityofChicago":UniversityofChicago,
        "AdamCurry":AdamCurry,
        "JDSupra":JDSupra,
        "UKGovernment":UKGovernment,
        "Investopedia":Investopedia,
        "Vox":Vox,
        "SouthChinaMorningPost":SouthChinaMorningPost,
        "OEMLubeNews":OEMLubeNews,
        "PRNewswire":PRNewswire,
        "FutureMarketInsights":FutureMarketInsights,
        "ManufacturingOperationsTechnologyViewpoints":ManufacturingOperationsTechnologyViewpoints,
        "CSIS":CSIS,
        "EdgeandOdds":EdgeandOdds,
        "maltawindscom":maltawindscom,
        "iamericas":iamericas,
        "cpzulia":cpzulia,
        "farms":farms,
        "LegalInsurrection":LegalInsurrection,
        "IFT":IFT,
        "InternationalBanker":InternationalBanker,
        "bankofcanada":bankofcanada,
        "KoenigInvestmentAdvisory":KoenigInvestmentAdvisory,
        "Europa":Europa,
        "JachinCapital":JachinCapital,
        "WellsFargo":WellsFargo,
        "ethicalconsumer":ethicalconsumer,
        "Citibank":Citibank,
        "CornellUniversity":CornellUniversity,
        "arabellaadvisors":arabellaadvisors,
        "CriticalThreats":CriticalThreats,
        "Fitch":Fitch,
        "prsync":prsync,
        "PhysicsWorld":PhysicsWorld,
        "RenewableEnergyWorld":RenewableEnergyWorld,
        "BBCNewsTechnology":BBCNewsTechnology,
        "edienet":edienet,
        "RussiaBeyondTheHeadlines":RussiaBeyondTheHeadlines,
        "Politico":Politico,
        "TechTimes":TechTimes,
        "WoodMcKenzie":WoodMcKenzie,
        "threeDPrintingProgress":threeDPrintingProgress,
        "ihsmarkit":ihsmarkit,
        "GizmodoAustralia":GizmodoAustralia,
        "TheNation":TheNation,
        "Farmscom":Farmscom,
        "McKinseyCompany":McKinseyCompany,
        "TheGuardian":TheGuardian,
        "ResourcesfortheFuture":ResourcesfortheFuture,
        "satprnews":satprnews,
        "GreenBiz":GreenBiz,
        "CNBC":CNBC ,
        "wwwnarendramodiin":wwwnarendramodiin,
        "CNNMoney":CNNMoney,
        "EIU":EIU,
        "Euromoney":Euromoney,
        "gasstrategies":gasstrategies,
        "Carscoza":Carscoza,
        "europeanclimate":europeanclimate,
        "AustralianGovernment":AustralianGovernment,
        "TeleTrade":TeleTrade,
        "BloombergNewEnergyFinance":BloombergNewEnergyFinance,
        "TheEconomist":TheEconomist,
        "PhysOrg":PhysOrg,
        "djsresearch":djsresearch,
        "nbk":nbk,
        "Guardian":Guardian,
        "cargill":cargill,
        "Worldly":Worldly,
        "UtilityDive":UtilityDive,
        "newscientist":newscientist,
        "westpandi":westpandi,
        "IASTOPPERS":IASTOPPERS,
        "THISDAYLIVE":THISDAYLIVE,
        "veteranstoday":veteranstoday,
        "thespanisheconomy":thespanisheconomy,
        "biologicaldiversity":biologicaldiversity,
        "portfolioticker":portfolioticker,
        "MITTechnologyReview":MITTechnologyReview,
        "FoodQualityNewscom":FoodQualityNewscom,
        "TheConversation":TheConversation,
        "WorldBankGroup":WorldBankGroup,
        "TheCable":TheCable,
        "FutureEarth":FutureEarth,
        "CarbonBrief":CarbonBrief,
        "Wikipedia":Wikipedia,
        "NWF":NWF,
        "USDA":USDA,
        "energyglobal":energyglobal,
        "IEAorg":IEAorg,
        "PwC":PwC,
        "metalprices":metalprices,
        "GEReports":GEReports,
        "ProjectSyndicate":ProjectSyndicate,
        "InteriorDesign":InteriorDesign,
        "idccommunity":idccommunity,
        "ScienceDaily":ScienceDaily,
        "TheMainichi":TheMainichi,
        "economy":economy,
        "Drillordrop":Drillordrop,
        "HuffingtonPost":HuffingtonPost,
        "Lawfare":Lawfare,
        "FutureseekLinkDigest":FutureseekLinkDigest,
        "EnvironmentalLeader":EnvironmentalLeader,
        "BusinessStandard":BusinessStandard,
        "ESPAS":ESPAS,
        "EulerHermes":EulerHermes,
        "amundi":amundi,
        "ebrd":ebrd,
        "DrydockMagazine":DrydockMagazine,
        "BorneoPostOnline":BorneoPostOnline,
        "FinanceMagnates":FinanceMagnates,
        "fridaythinking":fridaythinking,
        "Newsweek":Newsweek,
        "ECFR":ECFR,
        "UniversityofLatvia":UniversityofLatvia,
        "FutureTimeline":FutureTimeline,
        "allianzglobalinvestors":allianzglobalinvestors,
        "controleng":controleng,
        "inputsmonitor":inputsmonitor,
        "Planetsave":Planetsave ,
        "agriworldsa":agriworldsa,
        "globalmoneytrends":globalmoneytrends,
        "Oxfam":Oxfam,
        "Gartner":Gartner,
        "clientadvisoryservices":clientadvisoryservices,
        "IMF":IMF,
        "EcoBusinesscom":EcoBusinesscom,
        "ChannelNewsAsia":ChannelNewsAsia,
        "WarontheRocks":WarontheRocks,
        "biomassmagazine":biomassmagazine,
        "ThinkProgress":ThinkProgress,
        "No2NuclearPower":No2NuclearPower,
        "ogauthority":ogauthority,
        "IBEF":IBEF,
        "ProspectsforDevelopment":ProspectsforDevelopment,
        "EngineeringNews":EngineeringNews,
        "NDTV":NDTV,
        "AfricanDevelopmentBank":AfricanDevelopmentBank,
        "Aljazeeracom":Aljazeeracom,
        "worldenergy":worldenergy,
        "cloudfront":cloudfront,
        "Zawya":Zawya,
        "FAO":FAO,
        "VOA":VOA,
        "HospitalityTrends":HospitalityTrends,
        "saltlakecityheadlines":saltlakecityheadlines,
        "TheTickerTape":TheTickerTape,
        "TheGlobeandMail":TheGlobeandMail,
        "AgWebTheHomePageofAgriculture":AgWebTheHomePageofAgriculture,
        "CAFrackFacts":CAFrackFacts,
        "murc":murc,
        "FastCoExist":FastCoExist,
        "ScienceNews":ScienceNews,
        "Quartz":Quartz,
        "Total":Total,
        "globalizationpartners":globalizationpartners,
        "WashingtonPost":WashingtonPost,
        "InsideClimateNews":InsideClimateNews,
        "polymerspaintcolourjournal":polymerspaintcolourjournal,
        "njccnm":njccnm,
        "IISS":IISS,
        "TheAtlantic":TheAtlantic,
        "InnovationsReport":InnovationsReport,
        "Nature":Nature,
        "CushmanWakefield":CushmanWakefield,
        "Maplecroft":Maplecroft,
        "PredictiveAnalyticsTimes":PredictiveAnalyticsTimes,
        "McKinseyQuarterly":McKinseyQuarterly,
        "CountriescomGlobalContent":CountriescomGlobalContent,
        "TheMarketMogul":TheMarketMogul,
        "knomad":knomad,
        "UNESCO":UNESCO,
         "GlobalMeatNews.com":GlobalMeatNewscom,
         "MotorMagazine":MotorMagazine,
         "MENAForum":MENAForum,
         "BlueandGreenTomorrow":BlueandGreenTomorrow,
         "valburyresearch":valburyresearch,
         "HBR":HBR,
         "NanotechnologyInnovation":NanotechnologyInnovation,
         "oilvoice":oilvoice,
         "ecesr":ecesr,
         "Freedonia":Freedonia,
         "ethicalmarkets":ethicalmarkets,
         "ClimateNewsNetwork":ClimateNewsNetwork,
         "OPEC":OPEC,
         "INSEADKnowledge":INSEADKnowledge,
         "CIO":CIO,
         "InstitutionalInvestor":InstitutionalInvestor,
         "SocietyofMotorManufacturersandTradersSMMT":SocietyofMotorManufacturersandTradersSMMT,
         "worldculturepictorial":worldculturepictorial,
         "globalfueleconomy":globalfueleconomy,
         "LiveMint":LiveMint,
         "g7g20":g7g20,
         "Mast":Mast,
         "ReadWrite":ReadWrite,
         "LNG":LNG,
         "EuropeanCentralBank":EuropeanCentralBank,
         "IndustrialControlSecurity":IndustrialControlSecurity,
         "VeriskMaplecroft":VeriskMaplecroft,
         "ETEnergyworldcom":ETEnergyworldcom,
         "briandcolwell":briandcolwell,
         "DWCOM":DWCOM,
         "Elsevier":Elsevier,
         "MAPI":MAPI,
         "DaysOfYear":DaysOfYear,
        "VirginAtlantic":VirginAtlantic,
        "GovernmentofIreland":GovernmentofIreland,
        "TheEngineer":TheEngineer,
        "ISA":ISA,
        "EnergyTomorrow":EnergyTomorrow,
        "Justmeans":Justmeans,
        "KhaleejTimes":KhaleejTimes,
        "Innovaro":Innovaro,
        "FutureinFocus":FutureinFocus,
        "WhatsNext":WhatsNext,
        "StanfordNews":StanfordNews,
        "MiddleEastOnline":MiddleEastOnline,
        "NeonNettle":NeonNettle,
        "HandelsblattGlobal Edition":HandelsblattGlobalEdition,
        "EENews":EENews,
        "before":before,
        "aswm":aswm,
        "Shenandoah":Shenandoah,
        "DigitalistMagazine":DigitalistMagazine,
        "EPA":EPA,
        "Azonano":Azonano,
        "NationalGeographicSocietyblogs":NationalGeographicSocietyblogs,
        "IER":IER,
        "OceanAcidification":OceanAcidification,
        "SmartGridObserver":SmartGridObserver,
        "Freenewspos":Freenewspos,
        "AHDB":AHDB,
        "SlideShare":SlideShare,
        "VITATechnologies":VITATechnologies,
        "WallStreetDaily":WallStreetDaily,
        "Bearnobull":Bearnobull,
        "CCNFinancialBitcoinCryptocurrencyNews":CCNFinancialBitcoinCryptocurrencyNews,
        "IRENA":IRENA,
        "InternationalMonetaryFundIMF":InternationalMonetaryFundIMF,
        "GlobalInformationInc":GlobalInformationInc,
        "IDTECHINDEX":IDTECHINDEX,
        "TheJamestownFoundation":TheJamestownFoundation,
        "savepassamaquoddybay":savepassamaquoddybay,
        "atradius":atradius,
        "dailyquiddity":dailyquiddity,
        "bankofengland":bankofengland,
        "Futurity":Futurity,
        "BusinessGreen":BusinessGreen,
        "AboutBestBinaryOptionsStrategy":AboutBestBinaryOptionsStrategy,
        "IHSEngineering360":IHSEngineering360,
        "EuropeanCouncil":EuropeanCouncil,
        "ActivistPost":ActivistPost,
        "Newsletter":Newsletter,
        "USEnvironmentalProtectionAgency":USEnvironmentalProtectionAgency,
        "GlobalMoneyTrendsMagazine":GlobalMoneyTrendsMagazine,
        "CAJNewsAfrica":CAJNewsAfrica,
        "Planetizen":Planetizen,
        "CDC":CDC,
        "StrategyFormerlyBoozCompany":StrategyFormerlyBoozCompany,
        "PriceWaterhouseCoopers":PriceWaterhouseCoopers,
        "Newscom":Newscom,
        "BrookingsInstitute":BrookingsInstitute,
        "InnovateUK":InnovateUK,
        "TheArabGulfStatesInstituteWashington":TheArabGulfStatesInstituteWashington,
        "EmbeddedComputingDesign":EmbeddedComputingDesign,
        "EuropeanEnvironmentAgency":EuropeanEnvironmentAgency,
        "IndustryWeek":IndustryWeek,
        "AtlanticCouncil ":AtlanticCouncil ,
        "UKMinistryofDefense":UKMinistryofDefense,
        "FutureinFocus":FutureinFocus,
        "AustralianGovernmentDepartmentofDefence":AustralianGovernmentDepartmentofDefence,
        "MITSloanManagementReview":MITSloanManagementReview,
        "Scania Group":ScaniaGroup,
        "watercanada":watercanada,
        "CommonDreams":CommonDreams,
        "theicct":theicct,
        "nbp":nbp,
        "ThomsonReuters ":ThomsonReuters ,
        "UniversityChronicle":UniversityChronicle,
        "globalr2p":globalr2p,
        "Robothub":Robothub,
        "NewSecurityBeat":NewSecurityBeat,
        "betterenergy":betterenergy,
        "RealEstateProfessional":RealEstateProfessional,
        "MindCommerce":MindCommerce,
        "YahooFinance":YahooFinance,
        "PickensPlan":PickensPlan,
        "RUSI":RUSI,
        "HardinTibbs":HardinTibbs,
        "WorldHealth":WorldHealth,
        "environmentalpeacebuilding":environmentalpeacebuilding,
        "greenerearthnews":greenerearthnews,
        "conferenceseries":conferenceseries,
        "dailytexanonline":dailytexanonline,
        "EPSNews":EPSNews,
        "TheAmericanProspect":TheAmericanProspect,
        "Face2faceAfrica":Face2faceAfrica,
        "OilandGasJournal":OilandGasJournal,
        "Infracircle":Infracircle,
        "uschamber":uschamber,
        "energynewscyprus":energynewscyprus,
        }

    
    
    regions={
        "NorthernAmerica":NorthernAmerica,
        "CentralAmerica":CentralAmerica,
        "Africa":Africa,
        "Asia":Asia,
        "Europe":Europe,
        "SouthAmerica":SouthAmerica,
        "Oceania":Oceania,
        
    }
    
    
    
    country={
        "usa":usa,
        "Mexico": Mexico, 
        "Nigeria": Nigeria, 
        "Lebanon": Lebanon, 
        "Russsia": Russia, 
        "Saudi Arabia": SaudiArabia, 
        "Angola": Angola,
        "Egypt": Egypt,
        "South Africa": SouthAfrica, 
        "India": India, 
        "Ukraine": Ukraine, 
        "Azerbaijan": Azerbaijan, 
        'China': China, 
        'Colombia': Colombia, 
        'Niger': Niger, 
        'Libya': Libya, 
        'Brazil': Brazil, 
        'Mali': Mali, 
        'Indonesia': Indonesia, 
        'Iraq': Iraq, 
'Iran': Iran, 
'SouthSudan': SouthSudan, 
'Venezuela': Venezuela, 
'BurkinaFaso': BurkinaFaso, 
'Germany': Germany, 
'UnitedKingdom': UnitedKingdom, 
'Kuwait': Kuwait, 
'Canada': Canada, 
'Argentina': Argentina, 
'Japan': Japan, 
'Austria': Austria, 
'Spain': Spain, 
'Estonia': Estonia, 
'Hungary': Hungary, 
'Australia': Australia, 
'Morocco': Morocco, 
'Greece': Greece, 
'Qatar': Qatar, 
'Oman': Oman, 
'Liberia': Liberia, 
'Denmark': Denmark, 
'Malaysia': Malaysia, 
'Jordan': Jordan, 
'Syria': Syria, 
'Ethiopia': Ethiopia, 
'Norway': Norway, 
'Ghana': Ghana, 
'Kazakhstan': Kazakhstan, 
'Pakistan': Pakistan, 
'Gabon': Gabon, 
'uae': UAE, 
'Algeria': Algeria, 
'Turkey': Turkey, 
'Cyprus': Cyprus, 
'Belize': Belize, 
'Poland': Poland
}
    
    result = [{'label': key, 'value': '{{'+key+'}}'} for key in source.keys()]    
    
    context.update(topic)
    context.update(endyear)
    country.update(regions)
    return render(request,'index.html',{**context,**country})


