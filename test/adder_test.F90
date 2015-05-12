module adder_test

  use adder_module
  implicit none

  real :: tol = 1.e-6

  contains

!------------------------------------------------------------------------

    subroutine adder_test(adder, a, b, c)

      type(adder_type) :: adder
      real, intent(in) :: a, b, c

      call adder%init(a, b)
      call assert_equals(a, adder%a, tol, 'adder a')
      call assert_equals(b, adder%b, tol, 'adder b')
      call adder%add()
      call assert_equals(c, adder%result, tol, 'adder result')

    end subroutine adder_test

!------------------------------------------------------------------------

    subroutine test_add1

      call adder_test(1., 2., 3.)

    end subroutine test_add1

!------------------------------------------------------------------------

    subroutine test_add2()

      ! Adder test with comment

      call adder_test(-1., 3., 2.)

    end subroutine test_add2

!------------------------------------------------------------------------

    subroutine test_add3_setup
      ! Adder test with setup in title
      ! and a second comment line (should not be part of description)

      call adder_test(-2., 1., -1.)

    end subroutine test_add3_setup

!------------------------------------------------------------------------

    subroutine test_teardown_test()

      ! Adder test with teardown in title

      call adder_test(3., 2., 5.)

    end subroutine test_teardown_test

!------------------------------------------------------------------------

    SUBROUTINE TEST_OLDSCHOOL
    ! TEST ALL CAPS, MISSING END NAME
    CALL ADDER_TEST(5., 6., 11.)
    END SUBROUTINE

!------------------------------------------------------------------------

end module adder_test
