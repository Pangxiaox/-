
    function datetime()
	{
		let myDate = new Date();
		let Y = myDate.getFullYear();
		let M = myDate.getMonth() + 1;
		let D = myDate.getDate();
		let H = myDate.getHours();
		let Min = myDate.getMinutes();

		//处理月是一位的情况
		if((M + '').length === 1){
			M = '0' + (M + '');
		}

		//处理日是一位的情况
		if((D + '').length === 1){
			D = '0' + (D + '');
		}

		let curDayTime = Y+'-'+M+'-'+D+'T'+H+':'+Min;
    	let curDay = Y+'-'+M+'-'+D;

		$('#reportTime').val(curDayTime);
    	$('#medicalhistory_recordtime').val(curDayTime);
    	$('#admission_date').val(curDay);
	}