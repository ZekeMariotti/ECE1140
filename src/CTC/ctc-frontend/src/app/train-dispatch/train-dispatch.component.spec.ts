import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TrainDispatchComponent } from './train-dispatch.component';

describe('TrainDispatchComponent', () => {
  let component: TrainDispatchComponent;
  let fixture: ComponentFixture<TrainDispatchComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ TrainDispatchComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(TrainDispatchComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
