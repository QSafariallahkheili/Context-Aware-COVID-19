from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import Departments


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent



departments_mapping = {
    'code': 'code',
    'nom': 'nom',
    'area': 'area',
    'population': 'population',
    'pop_den': 'pop_den',
    'tot_death_field': 'tot_death_',
    'tot_infect': 'tot_infect',
    'death_rate': 'death_rate',
    'lon': 'lon',
    'lat': 'lat',
    'geom': 'MULTIPOLYGON',
}

#dep_shp = BASE_DIR/ 'covidapp/data/aggregated.shp'
#dep_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'covidapp/data/aggregated.shp'))
def run(verbose=True):
    lm = LayerMapping(Departments, 'covidapp/data/aggregated.shp', departments_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)