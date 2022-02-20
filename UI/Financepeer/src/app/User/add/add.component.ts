import { Component, OnInit } from '@angular/core';
import { SharedService } from 'src/app/shared.service'

@Component({
  selector: 'app-add',
  templateUrl: './add.component.html',
  styleUrls: ['./add.component.css']
})
export class AddComponent implements OnInit {
  filename!: string;
  path!:string;
  constructor(private service: SharedService) { }

  ngOnInit(): void {
  }

  addData(){
    var val = {filename:this.filename,
              path:this.path
              };

    this.service.addUser(val).subscribe(res=>{
      alert(res.toString());
    });
  }
  uploadPhoto(event:any){
    var file=event.target.files[0];
    const formData:FormData=new FormData();
    formData.append('uploadedFile',file,file.name);

    this.service.uploadfile(formData).subscribe((data:any)=>{
      this.filename=data.toString();
      this.path=this.service.fileUrl+this.filename;
    })
  }
}
// kjbui

