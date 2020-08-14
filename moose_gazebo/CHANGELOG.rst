^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package moose_gazebo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.1.3 (2020-08-14)
------------------
* Add the yaw argument to spawn_moose
* Rename spawn launch (`#5 <https://github.com/moose-cpr/moose_simulator/issues/5>`_)
  * Add the scripts folder to the install target too
  * Rename moose_sim to spawn_moose to stay consistent with the recent changes for the new sim environments
  * Remove the duplicate scripts from the install paths
* [moose_gazebo] Minor clean-up.
  - Removed env_run since it wasn't used
  - Dropped .py
  - Updated install in CMakeLists.txt
* Contributors: Chris I-B, Chris Iverach-Brereton, Tony Baltovski

0.1.2 (2020-02-04)
------------------
* Add the config directory to the install target; omitting it prevents the moose_world.launch from launching correctly
* Contributors: Chris I-B, Tony Baltovski

0.1.1 (2020-01-09)
------------------
* [moose_gazebo] Updated dependencies.
* Contributors: Tony Baltovski

0.1.0 (2019-12-17)
------------------
* Merge pull request `#1 <https://github.com/moose-cpr/moose_simulator/issues/1>`_ from dniewinski/gazebo_cleanup
  Gazebo cleanup
* Added script install
* Made a dummy keyswitch node to still use the same mux setup as the robot
* Using moose_description instead of duplicating description
* Merge branch 'master' into 'master'
  Initial Moose simulator
  See merge request research/moose_simulator!1
* Initial Moose simulator
* Contributors: Dave Niewinski, Loic Azzalini, Tony Baltovski
