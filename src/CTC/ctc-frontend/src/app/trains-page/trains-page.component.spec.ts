import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TrainsPageComponent } from './trains-page.component';

describe('TrainsPageComponent', () => {
  let component: TrainsPageComponent;
  let fixture: ComponentFixture<TrainsPageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ TrainsPageComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(TrainsPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
