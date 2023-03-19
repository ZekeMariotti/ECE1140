import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CTCSimulationComponent } from './ctc-simulation.component';

describe('CTCSimulationComponent', () => {
  let component: CTCSimulationComponent;
  let fixture: ComponentFixture<CTCSimulationComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CTCSimulationComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CTCSimulationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
