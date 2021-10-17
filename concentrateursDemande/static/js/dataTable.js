    $(document).ready(function() {
        var table1 = $('#dataTable1').DataTable( {
            "responsive": true,
            "dom": 'lfrtip',
            "language": {"url": "https://cdn.datatables.net/plug-ins/1.11.3/i18n/ar.json"},
            "columnDefs": [ {"targets": [1],"visible": false},
                            {"targets": [3],"visible": false},
                            {"targets": [5],"visible": false},
                            {"targets": [6],"visible": false},
                            {"targets": [8],"visible": false},
                            {"targets": [10],"visible": false},
                            {"targets": [14],"visible": false},
                           ],
        } ); 


        var table2 = $('#dataTable2').DataTable( {

            "responsive": true,
            "dom": 'lfrtip',
            "language": {"url": "https://cdn.datatables.net/plug-ins/1.11.3/i18n/ar.json"},
            "columnDefs": [ {"targets": [3],"visible": false},
                            {"targets": [5],"visible": false},
                            {"targets": [6],"visible": false},
                            {"targets": [7],"visible": false},
                            {"targets": [8],"visible": false},
                            {"targets": [10],"visible": false},
                           ],
        } ); 


        var table = $('#dataTable').DataTable( {
            "responsive": true,
            "language": {"url": "https://cdn.datatables.net/plug-ins/1.11.3/i18n/ar.json"}
        } ); 


        $('a.dropdown-item').on( 'click', function (e) {
            e.preventDefault();
            var column = table1.column( $(this).attr('data-column') );
            column.visible( ! column.visible() );
        });


        $('a.dropdown-item').on( 'click', function (e) {
            e.preventDefault();
            var column = table2.column( $(this).attr('data-column') );
            column.visible( ! column.visible() );
        }); 

    } );