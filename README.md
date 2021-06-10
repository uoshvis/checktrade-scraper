# checktrade-scraper
Checktrade scraper example. Consumes checktrade API to parse data by postcode.


To run scraper:
```
scrapy crawl checktrade -o output_example.csv -t csv
```

Output file: *output_example.csv*

**Output data example:**

|cat_label|company_name                       |email                                    |landline_phone|mobile_phone|postal_code|unique_name              |
|---------|-----------------------------------|-----------------------------------------|--------------|------------|-----------|-------------------------|
|Builder  |W&T Building Group                 |N/A                                      |N/A           |07488 842319|CF10 2NX   |WAndTBuildingGroup969108 |
|Builder  |SAL BUILDING SERVICES LTD          |N/A                                      |01443 806606  |07488 850516|CF10 2NX   |SalBuildingServices      |
|Builder  |Emerald Green Group Ltd            |N/A                                      |N/A           |07488 830744|CF10 2NX   |EmeraldGreenGroup991074  |
|Builder  |AP Property Preservation           |APPropertyPreservation@checkatrade.co.uk |N/A           |07458 187637|CF10 2NX   |APPropertyPreservation   |
|Builder  |C N C Renovations                  |N/A                                      |01873 777228  |07488 841482|CF10 2NX   |CNCRenovations971085     |
|Builder  |J A Unlimited Services             |JAUnServices@checkatrade.co.uk           |01594 806898  |07458 189550|CF10 2NX   |JAUnServices             |
|Builder  |TBI Maintenance Ltd                |TBIMaintenanceLtd888398@checkatrade.co.uk|N/A           |07488 819874|CF10 2NX   |TbiMaintenance           |
|Builder  |Collins Build Ltd                  |Collinsbuild@checkatrade.co.uk           |N/A           |07458 174663|CF10 2NX   |Collinsbuild             |
|Builder  |Weagan Building Contractors Limited|N/A                                      |N/A           |07488 837494|CF10 2NX   |WeaganBuildingContractors|



