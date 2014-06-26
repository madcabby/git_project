from mean_sightings import get_sightings
file = 'sightings_tab_sm.csv'

def test_water():
	watrec,watmean = get_sightings(file,'Water')
	assert watrec == 2, 'Number of records for water is wrong.'
	assert watmean == 17, 'Mean for water is wrong'

def test_Clay():
        clayrec,claymean = get_sightings(file,'Clay')
        assert clayrec == 2, 'Number of records for clay is wrong.'
        assert claymean == 25.5, 'Mean for clay is wrong'
def test_not_present():
	norec,nomean = get_sightings(file,'Not present')
	assert norec == 0, 'Biosignature not present, has zero recs.'
	assert nomean == 0, 'Mean is not present for missing Biosig.'
