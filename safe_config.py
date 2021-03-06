basic_html = '''
<html>
    <h1>BWT API</h1>
    <ul>
        <li>Base URL /request</li>
        <li>Acceptable parameters:</li>
        <ul>
            <li><i>start_date</i> format: "YYYY-MM-DD", inclusive, ex: 2021-09-01</li>
            <li><i>end_date</i> same as above, can be combined</li>
            <li><i>id</i> integer, leave empty or submit 'all' for all</li>
            <li><i>district, region</i></li>
            <li>collection</li>
            
        </ul>
        <li>collections, <i>(beware, not all parameters work for all collections)</i></li>
        <ul>
            <li><b>running_merge</b>, default, no need to specify, all times, merged with baseline info</li>
            <ul>
                <li>utc</li>
                <li>crossing_id</li>
                <li>name</li>
                <li>wait</li>
                <li>timezone</li>
                <li>district</li>
                <li>region</li>
                <li>lat</li>
                <li>long</li>
            </ul>
            <li><b>latest_merged</b>, shows just the latest time for each of the crossings </li>
            <ul>
                <li>id</li>
                <li>name</li>
                <li>wait</li>
                <li>timezone</li>
                <li>district</li>
                <li>region</li>
                <li>lat</li>
                <li>long</li>
            </ul>
            <li><b>leg_map</b></li>mapping table use to link legacy system "CBSA Office" to crossing_id
            <ul>
                <li>CBSA_Office</li>
                <li>crossing_id</li>
            </ul>
            <li><b>baseline</b></li>, tombstone information on each crossing_id
            <ul>
                <li>id</li>
                <li>name</li>
                <li>province</li>
                <li>dest, GPS coord as string of the actual crossing</li>
                <li>origin, GPS coord as string of the start of the trip</li>
                <li>distance, in meters for the trip</li>
                <li>timeZone</li>
                <li>region</li>
                <li>district</li>
                <li>profile, integer (1,2,3) which determines update frequency</li>
            </ul>
            
        </ul>
    </ul>
</html>
'''