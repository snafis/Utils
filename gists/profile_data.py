import pathlib
import pandas_profiling
output_profile_path = pathlib.Path("reports/data-profiling/01-01-initial_data_profiling.html")
profile = pandas_profiling.ProfileReport(data)
profile.to_file(outputfile=output_profile_path.as_posix())