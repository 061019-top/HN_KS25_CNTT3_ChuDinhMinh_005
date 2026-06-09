def xet_tien_do(cv):
    cv["chenh_lech"] = cv["thuc_te"] - cv["du_kien"]
    if cv["chenh_lech"] < 0:
        cv["trang_thai"] = "Hoàn thành sớm"
    elif cv["chenh_lech"] == 0:
        cv["trang_thai"] = "Bình thường"
    elif 1 <= cv["chenh_lech"] <= 3:
        cv["trang_thai"] = "Cần tăng tốc"
    else:
        cv["trang_thai"] = "Quá hạn"

def hien_thi_danh_sach(danh_sach):
    print("========================= DANH SÁCH CÔNG VIỆC =========================")
    if len(danh_sach) == 0:
        print("Dự án chưa có công việc nào")
        return  
    print(f"{'Mã CV':<8} | {'Tên công việc':<25} | {'Nhân viên':<20} | {'Dự kiến':<8} | {'Thực tế':<8} | {'Chênh lệch':<12} | {'Trạng thái'}")
    for cv in danh_sach:
        print(f"{cv['ma_cv']:<8} | {cv['ten_cv']:<25} | {cv['nhan_vien']:<20} | {cv['du_kien']:<8} | {cv['thuc_te']:<8} | {cv['chenh_lech']:<12} | {cv['trang_thai']}")

def them_cong_viec(danh_sach):
    print("--- THÊM CÔNG VIỆC ---")
    while True:
        ma_cv = input("Nhập mã công việc: ")
        if ma_cv == "":
            print("Không được để trống")
        else:
            trung = False
            for cv in danh_sach:
                if cv["ma_cv"] == ma_cv:
                    trung = True
                    break
            if trung == True:
                print("Mã công việc đã tồn tại")
            else:
                break
                
    while True:
        ten_cv = input("Nhập tên công việc: ")
        if ten_cv == "":
            print("Không được để trống")
        else:
            break
            
    while True:
        nhan_vien = input("Nhập tên nhân viên: ")
        if nhan_vien == "":
            print("Không được để trống")
        elif nhan_vien.isdigit() == True:
            print("Tên nhân viên không được là số")
        else:
            break

    while True:
        du_kien = input("Nhập số ngày dự kiến: ")
        if du_kien.isdigit() == True:
            du_kien = int(du_kien)
            if du_kien >= 1:
                break
            else:
                print("Số ngày phải lớn hơn 0")
        else:
            print("Vui lòng nhập số nguyên")

    while True:
        thuc_te = input("Nhập số ngày thực tế: ")
        if thuc_te.isdigit() == True:
            thuc_te = int(thuc_te)
            if thuc_te >= 0:
                break
            else:
                print("Số ngày phải lớn hơn hoặc bằng 0 ")
        else:
            print("Vui lòng nhập số nguyên")
    cv_moi = {
        "ma_cv": ma_cv,
        "ten_cv": ten_cv,
        "nhan_vien": nhan_vien,
        "du_kien": du_kien,
        "thuc_te": thuc_te
    }
    xet_tien_do(cv_moi)
    danh_sach.append(cv_moi)
    print("Thêm công việc thành công!")

def cap_nhat_tien_do(danh_sach):
    print("--- CẬP NHẬT TIẾN ĐỘ ---")
    if len(danh_sach) == 0:
        print("Dự án chưa có công việc nào")
        return

    ma_tim = input("Nhập mã công việc cần cập nhật: ")
    tim_thay = False

    for cv in danh_sach:
        if cv["ma_cv"] == ma_tim:
            tim_thay = True
            print(f"Đang cập nhật cho: {cv['ten_cv']}")
            
            while True:
                nhan_vien = input("Nhập tên nhân viên mới: ")
                if nhan_vien == "":
                    print("Không được để trống")
                elif nhan_vien.isdigit() == True:
                    print("Tên không được là số")
                else:
                    cv["nhan_vien"] = nhan_vien
                    break
                    
            while True:
                du_kien = input("Nhập số ngày dự kiến mới: ")
                if du_kien.isdigit() == True:
                    du_kien = int(du_kien)
                    if du_kien >= 1:
                        cv["du_kien"] = du_kien
                        break
                    else:
                        print("Số ngày phải lớn hơn 0")
                else:
                    print("Phải nhập số nguyên")
                    
            while True:
                thuc_te = input("Nhập số ngày thực tế mới: ")
                if thuc_te.isdigit() == True:
                    thuc_te = int(thuc_te)
                    if thuc_te >= 0:
                        cv["thuc_te"] = thuc_te
                        break
                    else:
                        print("Số ngày phải lớn hơn hoặc bằng 0")
                else:
                    print("Phải nhập số nguyên")
            
            xet_tien_do(cv)
            print("Cập nhật thành công")
            break
            
    if tim_thay == False:
        print("Không tìm thấy mã công việc này")

def xoa_cong_viec(danh_sach):
    print("--- XÓA CÔNG VIỆC ---")
    if len(danh_sach) == 0:
        print("Dự án chưa có công việc nào")
        return
        
    ma_xoa = input("Nhập mã công việc cần xóa: ")
    tim_thay = False
    for i in range(len(danh_sach)):
        if danh_sach[i]["ma_cv"] == ma_xoa:
            tim_thay = True
            xac_nhan = input("Bạn có chắc muốn xóa không? (Y/N): ")
            if xac_nhan == "Y" or xac_nhan == "y":
                danh_sach.pop(i)
                print("Đã xóa thành công")
            else:
                print("Đã hủy xóa")
            break
            
    if tim_thay == False:
        print("Không tìm thấy mã công việc này")

def tim_kiem_cong_viec(danh_sach):
    print("--- TÌM KIẾM ---")
    if len(danh_sach) == 0:
        print("Dự án chưa có công việc nào!")
        return
        
    tu_khoa = input("Nhập mã hoặc tên nhân viên cần tìm: ").lower()
    ket_qua = []
    for cv in danh_sach:
        if tu_khoa == cv["ma_cv"].lower() or tu_khoa in cv["nhan_vien"].lower():
            ket_qua.append(cv)      
    if len(ket_qua) > 0:
        hien_thi_danh_sach(ket_qua)
    else:
        print("Không tìm thấy kết quả phù hợp!")

def thong_ke_trang_thai(danh_sach):
    print("--- THỐNG KÊ ---")
    if len(danh_sach) == 0:
        print("Dự án chưa có công việc nào")
        return  
    som = 0
    binh_thuong = 0
    tang_toc = 0
    qua_han = 0
    for cv in danh_sach:
        if cv["trang_thai"] == "Hoàn thành sớm":
            som += 1
        elif cv["trang_thai"] == "Bình thường":
            binh_thuong += 1
        elif cv["trang_thai"] == "Cần tăng tốc":
            tang_toc += 1
        elif cv["trang_thai"] == "Quá hạn":
            qua_han += 1

    print(f"Tổng số công việc: {len(danh_sach)}")
    print(f"Hoàn thành sớm : {som}")
    print(f"Bình thường    : {binh_thuong}")
    print(f"Cần tăng tốc   : {tang_toc}")
    print(f"Quá hạn        : {qua_han}")

def main():
    danh_sach_cv = [
        {
            "ma_cv": "TS001",
            "ten_cv": "Thiet ke giao dien App",
            "nhan_vien": "Chu Dinh Minh",
            "du_kien": 10,
            "thuc_te": 14,
            "chenh_lech": 4,
            "trang_thai": "Quá hạn"
        }
    ]
    
    while True:
        chon = input("""
        ===== QUẢN LÝ TIẾN ĐỘ DỰ ÁN =====
        1. Hiển thị danh sách
        2. Thêm mới công việc
        3. Cập nhật tiến độ
        4. Xóa công việc
        5. Tìm kiếm
        6. Thống kê trạng thái
        7. Phân loại tự động
        8. Thoát
        Chọn chức năng (1-8): """)
                
        match chon:
            case "1":
                hien_thi_danh_sach(danh_sach_cv)
            case "2":
                them_cong_viec(danh_sach_cv)
            case "3":
                cap_nhat_tien_do(danh_sach_cv)
            case "4":
                xoa_cong_viec(danh_sach_cv)
            case "5":
                tim_kiem_cong_viec(danh_sach_cv)
            case "6":
                thong_ke_trang_thai(danh_sach_cv)
            case "7":
                pass
            case "8":
                print("Đã thoát chương trình")
                break
            case _:
                print("Chỉ được nhập từ 1 đến 8")

main()