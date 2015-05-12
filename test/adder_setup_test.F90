module adder_setup_test

  use adder_module
  use adder_test_module, only: adder_test
  implicit none

  real :: y = 0.0

contains

  !------------------------------------------------------------------------

  subroutine local_setup()

    y = 2.718

  end subroutine local_setup

  !------------------------------------------------------------------------

  subroutine teardown_adder

    y = 0.0

  end subroutine teardown_adder

  !------------------------------------------------------------------------

  subroutine test_1

    call adder_test(1., y, 3.718)

  end subroutine test_1

  !------------------------------------------------------------------------

  subroutine test_2()

    ! Test 2 with setup

    call adder_test(-1., y, 1.718)

  end subroutine test_2

  !------------------------------------------------------------------------

end module adder_setup_test
