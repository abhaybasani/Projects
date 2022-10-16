# --------------------------------------Phone information program---------------------------
class Phoneinfo:
    def getInfo(self):
        while True:
            try:
                from phonenumbers import timezone, geocoder, carrier, parse
                print("__________________________________________________")
                print("Example: 917856421458")
                number = input("[+]Enter your num with country code +__:")
                phone = parse("+" + number)
                # for know timezone of victem
                time = timezone.time_zones_for_number(phone)
                # known ISP
                simdetails = carrier.name_for_number(phone, "en")
                # known country by geo location
                country = geocoder.description_for_number(phone, "en")
                print("Time:>",time)
                print("Phone:>",phone)
                print("Sim details:>",simdetails)
                print("Country:>",country)
                # for longitude and latitude
                from opencage.geocoder import OpenCageGeocode
                geocoder = OpenCageGeocode('1a0e423f30a943f1be940684fe4c0d56')
                query = str(country)
                result = geocoder.geocode(query)
                latitude = result[0]['geometry']['lat']
                longitude = result[0]['geometry']['lng']
                print(f"Latitude:>{latitude}\nLongitude:>{longitude}")
                # ===========================================================================
                # for get .html page for gui map location
                # import folium
                # mymap=folium.Map(Location=[latitude,longitude],zoom_start=9)
                # folium.Marker([latitude,longitude],popup=country).add_to(mymap)
                # # save map in html file
                # mymap.save('victimLocation.html')
                # ====================================================================
            except ValueError:
                print("##please enter int type value! next time")
            except KeyboardInterrupt:
                print("program is finish. Thanks you.")
            except None:
                pass
			except:
				print("please contact the devloper Abhay")
phinfo=Phoneinfo()
phonfo.getInfo()