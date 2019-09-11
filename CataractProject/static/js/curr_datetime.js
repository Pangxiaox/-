var myDate = new Date();
var Y = myDate.getFullYear();
var M = myDate.getMonth() + 1;
var D = myDate.getDate();
var H = myDate.getHours();
var Min = myDate.getMinutes();

	//处理月是一位的情况
	if((M + '').length == 1){
		M = '0' + (M + '');
	}

	//处理日是一位的情况
	if((D + '').length == 1){
		D = '0' + (D + '');
	}

	var curDayTime =Y+'-'+M+'-'+D+'T'+H+':'+Min;
    var curDay = Y+'-'+M+'-'+D;

	$('#diagnosedate').val(curDayTime);
    $('#medicalhistory_recordtime').val(curDayTime);
    $('#admission_date').val(curDay);