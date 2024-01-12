console.log(1);

function hienThiThongTinChiTiet(){
    if(document.getElementById('chau2').style.display == 'none')
        document.getElementById('chau2').style.display = 'flex';
    else
        document.getElementById('chau2').style.display = 'none';
}
 function hienThiThanhToanTienMat(){
    if(document.getElementById('thanhToanTienMat').style.display == 'none')
        document.getElementById('thanhToanTienMat').style.display = 'flex';
    else
        document.getElementById('thanhToanTienMat').style.display = 'none';
}
function thanhToan() {
    var tienNhan = parseFloat(document.getElementById('c_tiennhan').value.replace('VND', '').replace(/\./g, ''));
    var tongTien = parseFloat(document.getElementById('tongtien').innerText.replace('VND', '').replace(/\./g, ''));
    if (tienNhan >= tongTien) {
        var tienThua = tienNhan - tongTien;
        document.getElementById('tiendu').innerText = tienThua.toLocaleString() + 'VND';
        alert('Thanh toán thành công! Tiền thừa: ' + tienThua.toLocaleString() + 'VND');
    } else {
         alert('Số tiền nhận không đủ để thanh toán!');
    }
}
