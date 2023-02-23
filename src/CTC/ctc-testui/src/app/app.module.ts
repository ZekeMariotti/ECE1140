import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { NavcontainerComponent } from './navcontainer/navcontainer.component';
import { WaysideBlocksComponent } from './wayside-blocks/wayside-blocks.component';
import { WaysideSwitchesComponent } from './wayside-switches/wayside-switches.component';
import { CTCLinesComponent } from './ctc-lines/ctc-lines.component';
import { CTCSimulationComponent } from './ctc-simulation/ctc-simulation.component';
import { FormsModule } from '@angular/forms';
import { CtcService } from './services/ctc.service';

@NgModule({
  declarations: [
    AppComponent,
    NavcontainerComponent,
    WaysideBlocksComponent,
    WaysideSwitchesComponent,
    CTCLinesComponent,
    CTCSimulationComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    NgbModule,
    FormsModule,
    HttpClientModule
  ],
  providers: [
    CtcService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
