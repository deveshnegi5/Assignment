import { Component, OnInit } from '@angular/core';
import { SharedService } from 'src/app/shared.service'

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  constructor(private service: SharedService) { }
  UserList: any = [];

  ngOnInit(): void {
    this.refreshUserList();
  }

  refreshUserList() {
    this.service.getUserList().subscribe(data => {
      this.UserList = data;
    });
  }
}
