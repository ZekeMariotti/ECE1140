import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { BlocksPageComponent } from './blocks-page/blocks-page.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { SimulationControlsComponent } from './simulation-controls/simulation-controls.component';
import { TrainDispatchComponent } from './train-dispatch/train-dispatch.component';
import { TrainTableComponent } from './train-table/train-table.component';
import { TrainsPageComponent } from './trains-page/trains-page.component';

const routes: Routes = [
  {path: '', redirectTo: '/dashboard', pathMatch: 'full'},
  {path: 'dashboard', component: DashboardComponent},
  {path: 'blocks', component: BlocksPageComponent},
  {path: 'trains', component: TrainsPageComponent},
  {path: 'trains/dispatch', component: TrainDispatchComponent},
  {path: 'simulation', component: SimulationControlsComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
