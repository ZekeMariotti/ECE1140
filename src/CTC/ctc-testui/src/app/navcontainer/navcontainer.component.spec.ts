import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NavcontainerComponent } from './navcontainer.component';

describe('NavcontainerComponent', () => {
  let component: NavcontainerComponent;
  let fixture: ComponentFixture<NavcontainerComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ NavcontainerComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(NavcontainerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
