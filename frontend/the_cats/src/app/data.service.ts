import { Injectable } from '@angular/core';
import { ApiService } from './api.service';

@Injectable({
  providedIn: 'root'
})
export class DataService {

  private data: any[] = [];

  constructor(private apiService: ApiService) { }

  getData(): any[] {
    return this.data;
  }

  updateData(data: any[]): void {
    this.data = data;
  }

  fetchInitialData(): void {
    this.apiService.getData().subscribe((data: any[]) => {
      this.updateData(data);
    });
  }
}
