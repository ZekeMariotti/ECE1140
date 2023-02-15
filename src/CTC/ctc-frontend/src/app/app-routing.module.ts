import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { TrainTableComponent } from './train-table/train-table.component';

const routes: Routes = [
  {path: '', redirectTo: '/trains', pathMatch: 'full'},
  {path: 'trains', component: TrainTableComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
