import { ComponentFixture, TestBed } from '@angular/core/testing';

import { WaysideSwitchesComponent } from './wayside-switches.component';

describe('WaysideSwitchesComponent', () => {
  let component: WaysideSwitchesComponent;
  let fixture: ComponentFixture<WaysideSwitchesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ WaysideSwitchesComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(WaysideSwitchesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
