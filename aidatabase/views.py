from django.shortcuts import get_object_or_404, render
from .models import Person, Ai, Review, Source  # , Series
# from bokeh.plotting import figure, output_file, show
# from bokeh.embed import components
# from bokeh.models import ColumnDataSource, FactorRange, BoxSelectTool
# from bokeh.palettes import Spectral6
# from bokeh.transform import factor_cmap

def welcome(request):
    """
    fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
    years = ['2015', '2016', '2017']

    data = {    'fruits'    : fruits,
                '2015'      : [2, 1, 4, 3, 2, 4],
                '2016'      : [5, 3, 3, 2, 4, 6],
                '2017'      : [3, 2, 4, 4, 5, 3] 
                }

    x = [ (fruit, year) for fruit in fruits for year in years]
    counts = sum(zip(data['2015'], data['2016'], data['2017']), ())

    source = ColumnDataSource(data=dict(x=x, counts=counts))
    plot = figure(x_range=FactorRange(*x), plot_height=250, title="Fruit Counts by Year",
        toolbar_location="below", 
        tools = "pan,wheel_zoom,box_zoom,reset")
    plot.add_tools(BoxSelectTool(dimensions="width"))
    #plot.add_tools(WheelZoomTool())
    plot.vbar(x='x', top='counts', width=0.9, source=source, line_color="white",
        fill_color=factor_cmap('x', palette=Spectral6, factors=years, start=1, end=2))

    plot.y_range.start = 0
    plot.x_range.range_padding = 0.1
    plot.xaxis.major_label_orientation = 1
    plot.xgrid.grid_line_color = None

    script, div = components(plot)
    return render(request, 'aidatabase/welcome.html', {'script': script, 'div': div})
    """
    return render(request, 'aidatabase/welcome.html')

def thesis(request):
    return render(request, 'aidatabase/thesis.html')

def project(request):
    return render(request, 'aidatabase/project.html')

def presentations(request):
    return render(request, 'aidatabase/presentations.html')

def links(request):
    return render(request, 'aidatabase/links.html')

def contact(request):
    return render(request, 'aidatabase/contact.html')

def imprint(request):
    return render(request, 'aidatabase/imprint.html')

def privacy(request):
    return render(request, 'aidatabase/privacy.html')

def ai_detail(request, ai_id):
    ai = get_object_or_404(Ai, pk=ai_id)
    reviews = Review.objects.filter(ai_id=ai.ai_id)
    source = Source.objects.get(source_id=ai.source_id.source_id)
    return render(request, 'aidatabase/ai_detail.html', {'ai': ai, 'reviews': reviews, 'source': source})

def ais(request):
    ais = Ai.objects.all().order_by("name")
    return render(request, 'aidatabase/ais.html', {'ais': ais})

def source_detail(request, source_id):
    source = get_object_or_404(Source, pk=source_id)
    ais = Ai.objects.filter(source_id=source.source_id).order_by("name")
    creators = source.creator.all()
    return render(request, 'aidatabase/source_detail.html', {'source': source, 'ais': ais, 'creators': creators})

def sources(request):
    sources = Source.objects.all().order_by("publish_year")
    result = []
    for s in sources:
        item = {}
        item["source"] = s
        item["creators"] = s.creator.all()
        result.append(item)
    return render(request, 'aidatabase/sources.html', {'result': result})

def person_detail(request, id):
    person = get_object_or_404(Person, person_id=id)
    sources = Source.objects.filter(creator=person.person_id).order_by("publish_year")
    return render(request, 'aidatabase/person_detail.html', {'person': person, 'sources': sources})

def persons(request):
    persons = Person.objects.all().order_by("lastname")
    return render(request, 'aidatabase/persons.html', {'persons': persons})
'''
def series_detail(request):
    # ...
    return render(request, 'series_detail.html', {'series': series})
'''
'''
def series(request, series_id):
    series = get_object_or_404(Series, pk=series_id)
    # ...
    return render(request, 'series.html', {'series': series})
'''
