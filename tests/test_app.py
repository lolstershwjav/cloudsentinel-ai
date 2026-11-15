from app import Telemetry, detect, explain

def test_authentication_alert():
    alerts=detect([Telemetry(45,6,30,'team-a'),Telemetry(55,0,32,'team-b')])
    assert alerts[0]['tenant']=='team-a'
    assert 'authentication' in explain(alerts[0])

def test_empty():
    assert detect([])==[]
