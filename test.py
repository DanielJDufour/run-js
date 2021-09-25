import os
import shutil
import unittest

import js

# before any tests are run
if os.path.isfile("package.json"):
    os.remove("package.json")
if os.path.isfile("package-lock.json"):
    os.remove("package-lock.json")
if os.path.isdir("package-lock.json"):
    shutil.rmtree("./node_modules")


class TestCases(unittest.TestCase):
    def test_top_level_with_array_arg(self):
        result = js["fast-min"]([1, 2, 3])
        self.assertEqual(result, 1)

    def test_top_level_with_string_arg(self):
        proj4string = "+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0 +k=1.0 +units=m +nadgrids=@null +wktext  +no_defs"
        result = js["get-epsg-code"](proj4string)
        self.assertEqual(result, 3857)

    def test_require_path_within_pkg(self):
        serialize_basic_csv = js["rle-serializers/serialize_basic_csv"]
        result = serialize_basic_csv([5, 3, 1, 8, 2, 0])
        self.assertEqual(result, "5,3,1,8,2,0")

    # test usage of keyword "from"
    def test_top_level_with_keyword(self):
        result = js["reproject-bbox"](
            {"bbox": [-122.51, 40.97, -122.34, 41.11], "from": 4326, "to": 3857}
        )
        self.assertEqual(
            result,
            [
                -13637750.817083945,
                5007917.677222896,
                -13618826.503649088,
                5028580.202823918,
            ],
        )

    def test_async(self):
        url = "https://s3-us-west-2.amazonaws.com/planet-disaster-data/hurricane-harvey/SkySat_Freeport_s03_20170831T162740Z3.tif"
        result = js.georaster(url)
        self.assertEqual(result["projection"], 32615)

    def test_install_prompt(self):
        result = js["faster-median"]({"nums": [1, 2, 3, 4, 5]})
        self.assertEqual(result, 3)

    def test_parse_any_int(self):
        result = js["parse-any-int"]("1,2345.0")
        self.assertEqual(result, 12345)

    def test_org_package(self):
        result = js["@turf/area"](
            {
                "type": "Feature",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [[125, -15], [113, -22], [154, -27], [144, -15], [125, -15]]
                    ],
                },
            }
        )
        self.assertEqual(result, 3339946239196.927)


if __name__ == "__main__":
    unittest.main()
