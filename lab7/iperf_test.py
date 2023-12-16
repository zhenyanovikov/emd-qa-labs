import parser


class TestSuite:
    def test_iperf3_client_connection(self, client):
        out, err = client
        assert err == b''
        parsed = parser.parse(out)
        assert float(parsed['Bitrate']) > 0
        assert float(parsed['Bitrate']) < 1000000000
