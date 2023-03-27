import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClient, HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { TrainTableComponent } from './train-table/train-table.component';
import { HeaderComponent } from './header/header.component';
import { TrainsPageComponent } from './trains-page/trains-page.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { BlocksPageComponent } from './blocks-page/blocks-page.component';
import { BlockTableComponent } from './block-table/block-table.component';
import { SimulationControlsComponent } from './simulation-controls/simulation-controls.component';
import { TrainDispatchComponent } from './train-dispatch/train-dispatch.component';

@NgModule({
  declarations: [
    AppComponent,
    TrainTableComponent,
    HeaderComponent,
    TrainsPageComponent,
    DashboardComponent,
    BlocksPageComponent,
    BlockTableComponent,
    SimulationControlsComponent,
    TrainDispatchComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule,
    NgbModule,
    FormsModule,
    ReactiveFormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
