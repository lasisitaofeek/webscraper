import csv

def write_to_csv(data = None, fields_to_exclude = None, filePath='scraped_data.csv'):
    if data is None or len(data) == 0:
        raise IOError("There is no data to write to the store.") #, *args, **kwargs)
    #end if
    
    if fields_to_exclude is None:
        fields_to_exclude = []
    #end if

    # compose [fields] that should be written to the .csv file
    # removing those that are in 'fields_to_exclude'
    fields = [k for k, v in data[0].items() if k not in fields_to_exclude]
    try:
        # open the .csv file for writing
        writer = csv.writer(open(filePath, 'w', newline=''))

        # write the column headers
        writer.writerow(fields)

        """    
        # for each dictionary item in the list
        for item in data:
            # pick only values in the current item for the fields not excluded
            row = [v for k, v in item.items() if k in fields]
            # write the row to the .csv file
            writer.writerow(row)
        """
        rows = []
        for idx in range(len(data)):
            # pick only values in the current item for the fields not excluded
            row = [v for k, v in data[idx].items() if k in fields]
            # write the row to the .csv file
            rows.append(row)

        writer.writerows(rows)

    except (IOError, OSError) as ex:
        raise ex
#end function

if __name__ == "__main__":
    data = [
        {'binder': '', 'brand': '', 'color': '', 'filler': '', 'html_attributes': '', 'labels': '', 'manufacturer': '', 'name': "Cigar Aficionado's Best Bargain Cigars of 2016, 10-Cigar Sampler", 'notes': 'Every year, Cigar Aficionado releases a list of Best Buys, cigars that are top notch but sell for $6 or less. Here are 10 of the top rated cigars out of the 2016 list.', 'origin': '', 'photos': '//az571366.vo.msecnd.net/prodimgl/164513_0.jpg?dummy=164753640', 'price': None, 'profile': '', 'rating': '4.35', 'ratingCount': '4', 'shapes': '', 'smoking-notes': '', 'strength': '', 'productID': '164513', 'productURL': 'https://www.neptunecigar.com/cigars/cigar-aficionados-best-bargain-cigars-of-2016-27-cigar-sampler'}, 
        {'binder': '', 'brand': '', 'color': '', 'filler': '', 'html_attributes': '', 'labels': '', 'manufacturer': '', 'name': "Cigar Aficionado's Best Bargain Cigars of 2016, 10-Cigar Sampler", 'notes': 'Every year, Cigar Aficionado releases a list of Best Buys, cigars that are top notch but sell for $6 or less. Here are 10 of the top rated cigars out of the 2016 list.', 'origin': '', 'photos': '//az571366.vo.msecnd.net/prodimgl/164513_0.jpg?dummy=164753640', 'price': None, 'profile': '', 'rating': '4.35', 'ratingCount': '4', 'shapes': '', 'smoking-notes': '', 'strength': '', 'productID': '164513', 'productURL': 'https://www.neptunecigar.com/cigars/cigar-aficionados-best-bargain-cigars-of-2016-27-cigar-sampler'}, 
        {'binder': '', 'brand': '', 'color': '', 'filler': '', 'html_attributes': '', 'labels': '', 'manufacturer': '', 'name': "Cigar Aficionado's Best Bargain Cigars of 2016, 10-Cigar Sampler", 'notes': 'Every year, Cigar Aficionado releases a list of Best Buys, cigars that are top notch but sell for $6 or less. Here are 10 of the top rated cigars out of the 2016 list.', 'origin': '', 'photos': '//az571366.vo.msecnd.net/prodimgl/164513_0.jpg?dummy=164753640', 'price': None, 'profile': '', 'rating': '4.35', 'ratingCount': '4', 'shapes': '', 'smoking-notes': '', 'strength': '', 'productID': '164513', 'productURL': 'https://www.neptunecigar.com/cigars/cigar-aficionados-best-bargain-cigars-of-2016-27-cigar-sampler'}, 
        {'binder': '', 'brand': '', 'color': '', 'filler': '', 'html_attributes': '', 'labels': '', 'manufacturer': '', 'name': "Cigar Aficionado's Best Bargain Cigars of 2016, 10-Cigar Sampler", 'notes': 'Every year, Cigar Aficionado releases a list of Best Buys, cigars that are top notch but sell for $6 or less. Here are 10 of the top rated cigars out of the 2016 list.', 'origin': '', 'photos': '//az571366.vo.msecnd.net/prodimgl/164513_0.jpg?dummy=164753640', 'price': None, 'profile': '', 'rating': '4.35', 'ratingCount': '4', 'shapes': '', 'smoking-notes': '', 'strength': '', 'productID': '164513', 'productURL': 'https://www.neptunecigar.com/cigars/cigar-aficionados-best-bargain-cigars-of-2016-27-cigar-sampler'}
     ]
    try:
        write_to_csv(data, ["html_attributes", "filler", "smoking_notes", "binder", "brand", "color", "filler", "html_attributes", "labels", "manufacturer"])
    except (IOError, AttributeError, OSError) as ex:
        print("Unexpected error encountered while writing to the data store. Reason: ")
        print(ex)
    #end try
#end if