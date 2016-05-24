package jackpal.androidterm.test;

import jackpal.androidterm.Term;
import jackpal.androidterm.emulatorview.compat.KeycodeConstants;

import com.robotium.solo.*;
import android.test.ActivityInstrumentationTestCase2;


public class RobotiumTest extends ActivityInstrumentationTestCase2<Term> {
  	private Solo solo;
  	
  	public RobotiumTest() {
		super("jackpal.androidterm.Term", Term.class);
  	}

  	public void setUp() throws Exception {
        super.setUp();
		solo = new Solo(getInstrumentation());
		getActivity();
		System.gc();
  	}
  
   	@Override
   	public void tearDown() throws Exception {
        solo.finishOpenedActivities();
        super.tearDown();
  	}
  
	public void testRun() {
        //Wait for activity: 'jackpal.androidterm.Term'
		solo.waitForActivity(jackpal.androidterm.Term.class, 2000);
        //Sleep for 14037 milliseconds
		solo.sleep(700);
		solo.sendKey(KeycodeConstants.KEYCODE_L);
		solo.sendKey(KeycodeConstants.KEYCODE_S);
		solo.sendKey(KeycodeConstants.KEYCODE_ENTER);
		solo.sleep(800);
		solo.sendKey(KeycodeConstants.KEYCODE_P);
		solo.sendKey(KeycodeConstants.KEYCODE_W);
		solo.sendKey(KeycodeConstants.KEYCODE_D);
		solo.sendKey(KeycodeConstants.KEYCODE_ENTER);
		solo.sleep(900);
		solo.clickOnScreen(229.47011F, 131.82661F);
        //Sleep for 5101 milliseconds
		solo.sleep(801);
        //Click on (450.37448, 103.918816)
		solo.clickOnScreen(450.37448F, 103.918816F);
        //Sleep for 1746 milliseconds
		solo.sleep(646);
        //Click on (425.40915, 119.90633)
		solo.clickOnScreen(425.40915F, 119.90633F);
        //Sleep for 1023 milliseconds
		solo.sleep(723);
        //Click on (428.405, 121.90476)
		solo.clickOnScreen(428.405F, 121.90476F);
        //Sleep for 1100 milliseconds
		solo.sleep(700);
        //Click on (559.2233, 110.913345)
		solo.clickOnScreen(559.2233F, 110.913345F);
        //Wait for dialog
		solo.waitForDialogToOpen(5000);
        //Sleep for 925 milliseconds
		solo.sleep(925);
        //Click on (560.2219, 692.45905)
		solo.clickOnScreen(560.2219F, 692.45905F);
        //Sleep for 1295 milliseconds
		solo.sleep(795);
        //Click on (234.17476, 125.40202)
		solo.clickOnScreen(234.17476F, 125.40202F);
        //Sleep for 1805 milliseconds
		solo.sleep(805);
        //Click on (227.18446, 108.9149)
		solo.clickOnScreen(227.18446F, 108.9149F);
        //Sleep for 3026 milliseconds
		solo.sleep(926);
        //Click on (222.6907, 133.3958)
		solo.clickOnScreen(222.6907F, 133.3958F);
        //Sleep for 4628 milliseconds
		solo.sleep(628);
        //Click on (682.05273, 123.9032)
		solo.clickOnScreen(682.05273F, 123.9032F);
        //Sleep for 605 milliseconds
		solo.sleep(605);
        //Click on (426.40778, 120.90554)
		solo.clickOnScreen(426.40778F, 120.90554F);
        //Sleep for 721 milliseconds
		solo.sleep(721);
        //Click on (676.06104, 125.40202)
		solo.clickOnScreen(676.06104F, 125.40202F);
        //Sleep for 726 milliseconds
		solo.sleep(726);
        //Click on action bar item
		solo.clickOnActionBarItem(jackpal.androidterm.R.id.menu_window_list);
        //Wait for activity: 'jackpal.androidterm.WindowList'
		assertTrue("jackpal.androidterm.WindowList is not found!", solo.waitForActivity(jackpal.androidterm.WindowList.class));
        //Sleep for 1751 milliseconds
		solo.sleep(1751);
        //Click on (663.0791, 356.7213)
		solo.clickOnScreen(663.0791F, 356.7213F);
        //Sleep for 3755 milliseconds
		solo.sleep(755);
        //Press menu back key
		solo.goBack();
        //Sleep for 1607 milliseconds
		solo.sleep(607);
        //Click on (685.0486, 89.92974)
		solo.clickOnScreen(685.0486F, 89.92974F);
        //Sleep for 1533 milliseconds
		solo.sleep(533);
        //Click on action bar item
		solo.clickOnActionBarItem(jackpal.androidterm.R.id.menu_special_keys);
        //Wait for dialog
		solo.waitForDialogToOpen(5000);
        //Sleep for 1105 milliseconds
		solo.sleep(805);
        //Drag from (466.3523, 711.44415) to (513.2871, 206.83841)
		solo.drag(466.3523F, 513.2871F, 711.44415F, 206.83841F, 40);
        //Sleep for 1186 milliseconds
		solo.sleep(886);
        //Drag from (513.2871, 482.62296) to (468.1623, 827.33276)
		solo.drag(513.2871F, 468.1623F, 482.62296F, 827.33276F, 40);
        //Sleep for 1215 milliseconds
		solo.sleep(715);
        //Drag from (521.276, 934.2701) to (503.301, 655.4879)
		solo.drag(521.276F, 503.301F, 934.2701F, 655.4879F, 40);
        //Sleep for 1023 milliseconds
		solo.sleep(923);
        //Press menu back key
		solo.goBack();
        //Wait for dialog to close
		solo.waitForDialogToClose(5000);
        //Sleep for 2809 milliseconds
		solo.sleep(809);
        //Click on (682.05273, 87.931305)
		solo.clickOnScreen(682.05273F, 87.931305F);
        //Sleep for 1916 milliseconds
		solo.sleep(816);
        //Click on action bar item
		solo.clickOnActionBarItem(jackpal.androidterm.R.id.menu_reset);
        //Sleep for 2230 milliseconds
		solo.sleep(830);
        //Click on (682.81067, 117.66709)
		solo.clickOnScreen(682.81067F, 117.66709F);
        //Sleep for 1381 milliseconds
		solo.sleep(781);
        //Click on action bar item
		solo.clickOnActionBarItem(jackpal.androidterm.R.id.menu_toggle_soft_keyboard);
        //Sleep for 1317 milliseconds
		solo.sleep(717);
        //Click on (683.0514, 138.8915)
		solo.clickOnScreen(683.0514F, 138.8915F);
        //Sleep for 1222 milliseconds
		solo.sleep(622);
        //Click on action bar item
		solo.clickOnActionBarItem(jackpal.androidterm.R.id.menu_toggle_soft_keyboard);
        //Sleep for 2017 milliseconds
		solo.sleep(1017);
        //Click on (683.05133, 106.41686)
		solo.clickOnScreen(683.05133F, 106.41686F);
        //Sleep for 2590 milliseconds
		solo.sleep(590);
        //Click on action bar item
		solo.clickOnActionBarItem(jackpal.androidterm.R.id.menu_preferences);
        //Wait for activity: 'jackpal.androidterm.TermPreferences'
		assertTrue("jackpal.androidterm.TermPreferences is not found!", solo.waitForActivity(jackpal.androidterm.TermPreferences.class));
        //Sleep for 1668 milliseconds
		solo.sleep(668);
        //Drag from (564.2164, 473.62997) to (528.2663, 743.5426)
		solo.drag(564.2164F, 528.2663F, 473.62997F, 743.5426F, 40);
        //Sleep for 566 milliseconds
		solo.sleep(566);
        //Rotate the screen
		solo.setActivityOrientation(Solo.LANDSCAPE);
        //Sleep for 1844 milliseconds
		solo.sleep(844);
        //Rotate the screen
		solo.setActivityOrientation(Solo.PORTRAIT);
        //Sleep for 3581 milliseconds
		solo.sleep(881);
        //Drag from (461.35922, 830.35126) to (484.32733, 717.4395)
		solo.drag(461.35922F, 484.32733F, 830.35126F, 717.4395F, 40);
        //Click on (476.33844, 574.55115)
		solo.clickOnScreen(476.33844F, 574.55115F);
        //Wait for dialog
		solo.waitForDialogToOpen(5000);
        //Sleep for 731 milliseconds
		solo.sleep(731);
        //Drag from (447.37866, 828.35284) to (485.65704, 624.8526)
		solo.drag(447.37866F, 485.65704F, 828.35284F, 624.8526F, 40);
        //Sleep for 733 milliseconds
		solo.sleep(733);
        //Click on (493.31488, 712.4435)
		solo.clickOnScreen(493.31488F, 712.4435F);
        //Sleep for 2538 milliseconds
		solo.sleep(938);
        //Drag from (494.31348, 981.2334) to (515.7837, 744.41846)
		solo.drag(494.31348F, 515.7837F, 981.2334F, 744.41846F, 40);
        //Press menu back key
		solo.goBack();
        //Sleep for 1672 milliseconds
		solo.sleep(972);
        //Click on (678.0583, 110.913345)
		solo.clickOnScreen(678.0583F, 110.913345F);
        //Sleep for 983 milliseconds
		solo.sleep(983);
        //Click on action bar item
		solo.clickOnActionBarItem(jackpal.androidterm.R.id.menu_preferences);
        //Wait for activity: 'jackpal.androidterm.TermPreferences'
		assertTrue("jackpal.androidterm.TermPreferences is not found!", solo.waitForActivity(jackpal.androidterm.TermPreferences.class));
        //Sleep for 1146 milliseconds
		solo.sleep(946);
        //Drag from (528.2663, 471.63153) to (497.3093, 737.7649)
		solo.drag(528.2663F, 497.3093F, 471.63153F, 737.7649F, 40);
        //Sleep for 587 milliseconds
		solo.sleep(587);
        //Click on (431.40085, 649.49255)
		solo.clickOnScreen(431.40085F, 649.49255F);
        //Wait for dialog
		solo.waitForDialogToOpen(5000);
        //Sleep for 1139 milliseconds
		solo.sleep(939);
        //Drag from (508.29404, 492.61514) to (499.63687, 797.5899)
		solo.drag(508.29404F, 499.63687F, 492.61514F, 797.5899F, 40);
        //Sleep for 613 milliseconds
		solo.sleep(613);
        //Drag from (460.36063, 561.5613) to (481.33588, 826.0286)
		solo.drag(460.36063F, 481.33588F, 561.5613F, 826.0286F, 40);
        //Sleep for 738 milliseconds
		solo.sleep(738);
        //Drag from (461.35922, 564.55896) to (449.3759, 670.40936)
		solo.drag(461.35922F, 449.3759F, 564.55896F, 670.40936F, 40);
        //Click on (505.29822, 283.7783)
		solo.clickOnScreen(505.29822F, 283.7783F);
        //Sleep for 909 milliseconds
		solo.sleep(909);
        //Click on (576.1997, 346.72913)
		solo.clickOnScreen(576.1997F, 346.72913F);
        //Sleep for 1256 milliseconds
		solo.sleep(956);
        //Drag from (646.10266, 361.7174) to (587.1845, 648.49335)
		solo.drag(646.10266F, 587.1845F, 361.7174F, 648.49335F, 40);
        //Sleep for 686 milliseconds
		solo.sleep(686);
        //Click on (573.2039, 189.35208)
		solo.clickOnScreen(573.2039F, 189.35208F);
        //Wait for dialog
		solo.waitForDialogToOpen(5000);
        //Sleep for 996 milliseconds
		solo.sleep(996);
        //Click on (436.39392, 780.3903)
		solo.clickOnScreen(436.39392F, 780.3903F);
        //Click on (476.8377, 327.74396)
		solo.clickOnScreen(476.8377F, 327.74396F);
        //Wait for dialog
		solo.waitForDialogToOpen(5000);
        //Sleep for 796 milliseconds
		solo.sleep(796);
        //Click on (461.35922, 774.395)
		solo.clickOnScreen(461.35922F, 774.395F);
        //Sleep for 504 milliseconds
		solo.sleep(504);
        //Click on (451.3731, 476.12805)
		solo.clickOnScreen(451.3731F, 476.12805F);
        //Wait for dialog
		solo.waitForDialogToOpen(5000);
        //Sleep for 1774 milliseconds
		solo.sleep(774);
        //Click on (426.90707, 813.3645)
		solo.clickOnScreen(426.90707F, 813.3645F);
        //Sleep for 997 milliseconds
		solo.sleep(797);
        //Drag from (543.2455, 825.35516) to (537.2029, 530.0552)
		solo.drag(543.2455F, 537.2029F, 825.35516F, 530.0552F, 40);
        //Sleep for 986 milliseconds
		solo.sleep(786);
        //Click on (610.1526, 553.5675)
		solo.clickOnScreen(610.1526F, 553.5675F);
        //Sleep for 771 milliseconds
		solo.sleep(771);
        //Click on (624.1332, 494.6136)
		solo.clickOnScreen(624.1332F, 494.6136F);
        //Sleep for 1085 milliseconds
		solo.sleep(985);
        //Drag from (642.1082, 776.39343) to (625.54834, 504.77136)
		solo.drag(642.1082F, 625.54834F, 776.39343F, 504.77136F, 40);
        //Sleep for 1555 milliseconds
		solo.sleep(555);
        //Drag from (538.25244, 679.4692) to (575.94763, 490.49542)
		solo.drag(538.25244F, 575.94763F, 679.4692F, 490.49542F, 40);
        //Sleep for 656 milliseconds
		solo.sleep(656);
        //Drag from (633.12067, 630.5074) to (624.1332, 483.62216)
		solo.drag(633.12067F, 624.1332F, 630.5074F, 483.62216F, 40);
        //Sleep for 777 milliseconds
		solo.sleep(777);
        //Drag from (499.30652, 759.40674) to (525.27045, 520.59326)
		solo.drag(499.30652F, 525.27045F, 759.40674F, 520.59326F, 40);
        //Sleep for 667 milliseconds
		solo.sleep(667);
        //Drag from (579.19556, 453.6456) to (535.2566, 801.3739)
		solo.drag(579.19556F, 535.2566F, 453.6456F, 801.3739F, 40);
        //Sleep for 675 milliseconds
		solo.sleep(675);
        //Drag from (494.31348, 508.60266) to (508.7635, 871.72925)
		solo.drag(494.31348F, 508.7635F, 508.60266F, 871.72925F, 40);
        //Sleep for 605 milliseconds
		solo.sleep(605);
        //Drag from (453.37033, 579.54724) to (523.2733, 903.79395)
		solo.drag(453.37033F, 523.2733F, 579.54724F, 903.79395F, 40);
        //Sleep for 624 milliseconds
		solo.sleep(924);
        //Click on (415.42303, 515.59717)
		solo.clickOnScreen(415.42303F, 515.59717F);
        //Wait for dialog
		solo.waitForDialogToOpen(5000);
        //Sleep for 3413 milliseconds
		solo.sleep(813);
        //Click on (562.2192, 1021.2022)
		solo.clickOnScreen(562.2192F, 1021.2022F);
        //Sleep for 2185 milliseconds
		solo.sleep(885);
        //Click on (492.31622, 507.60342)
		solo.clickOnScreen(492.31622F, 507.60342F);
        //Wait for dialog
		solo.waitForDialogToOpen(5000);
        //Sleep for 1261 milliseconds
		solo.sleep(861);
        //Click on (540.34076, 814.3638)
		solo.clickOnScreen(540.34076F, 814.3638F);
        //Sleep for 1319 milliseconds
		solo.sleep(819);
        //Press menu back key
		solo.goBack();
        //Sleep for 1397 milliseconds
		solo.sleep(997);
        //Click on (679.0569, 123.9032)
		solo.clickOnScreen(679.0569F, 123.9032F);
        //Sleep for 901 milliseconds
		solo.sleep(901);
        //Click on action bar item
		solo.clickOnActionBarItem(jackpal.androidterm.R.id.menu_preferences);
        //Wait for activity: 'jackpal.androidterm.TermPreferences'
		assertTrue("jackpal.androidterm.TermPreferences is not found!", solo.waitForActivity(jackpal.androidterm.TermPreferences.class));
        //Sleep for 2949 milliseconds
		solo.sleep(949);
        //Drag from (540.2497, 936.26855) to (553.2316, 690.4606)
		solo.drag(540.2497F, 553.2316F, 936.26855F, 690.4606F, 40);
        //Click on (482.3301, 576.54956)
		solo.clickOnScreen(482.3301F, 576.54956F);
        //Wait for dialog
		solo.waitForDialogToOpen(5000);
        //Sleep for 1793 milliseconds
		solo.sleep(793);
        //Drag from (524.27185, 591.53784) to (568.2108, 533.5831)
		solo.drag(524.27185F, 568.2108F, 591.53784F, 533.5831F, 40);
        //Sleep for 1151 milliseconds
		solo.sleep(951);
        //Drag from (588.1831, 507.60342) to (541.2483, 1000.9003)
		solo.drag(588.1831F, 541.2483F, 507.60342F, 1000.9003F, 40);
        //Sleep for 658 milliseconds
		solo.sleep(658);
        //Drag from (512.2885, 922.2795) to (502.30237, 605.5269)
		solo.drag(512.2885F, 502.30237F, 922.2795F, 605.5269F, 40);
        //Sleep for 1563 milliseconds
		solo.sleep(963);
        //Drag from (459.362, 868.3216) to (461.35922, 624.5121)
		solo.drag(459.362F, 461.35922F, 868.3216F, 624.5121F, 40);
        //Sleep for 2201 milliseconds
		solo.sleep(901);
        //Click on (557.7254, 924.7775)
		solo.clickOnScreen(557.7254F, 924.7775F);
        //Sleep for 3090 milliseconds
		solo.sleep(990);
        //Drag from (516.28296, 1012.2092) to (563.2178, 604.5277)
		solo.drag(516.28296F, 563.2178F, 1012.2092F, 604.5277F, 40);
        //Sleep for 998 milliseconds
		solo.sleep(798);
        //Drag from (517.28156, 918.2826) to (591.17896, 573.55194)
		solo.drag(517.28156F, 591.17896F, 918.2826F, 573.55194F, 40);
        //Sleep for 1113 milliseconds
		solo.sleep(113);
        //Drag from (559.2233, 967.2443) to (577.19836, 618.5168)
		solo.drag(559.2233F, 577.19836F, 967.2443F, 618.5168F, 40);
        //Sleep for 1757 milliseconds
		solo.sleep(757);
        //Drag from (509.29266, 953.25525) to (522.27466, 660.484)
		solo.drag(509.29266F, 522.27466F, 953.25525F, 660.484F, 40);
        //Sleep for 1907 milliseconds
		solo.sleep(907);
        //Press menu back key
		solo.goBack();
        //Sleep for 2369 milliseconds
		solo.sleep(369);
        //Click on (680.0555, 93.92662)
		solo.clickOnScreen(680.0555F, 93.92662F);
        //Sleep for 1322 milliseconds
		solo.sleep(322);
        //Click on action bar item
		solo.clickOnActionBarItem(jackpal.androidterm.R.id.menu_reset);
        //Sleep for 818 milliseconds
		solo.sleep(818);
        //Click on (679.0569, 115.90945)
		solo.clickOnScreen(679.0569F, 115.90945F);
        //Sleep for 913 milliseconds
		solo.sleep(913);
        //Click on action bar item
		solo.clickOnActionBarItem(jackpal.androidterm.R.id.menu_toggle_wakelock);
        //Sleep for 1041 milliseconds
		solo.sleep(1041);
        //Click on (675.0624, 127.40047)
		solo.clickOnScreen(675.0624F, 127.40047F);
        //Sleep for 1804 milliseconds
		solo.sleep(804);
        //Click on action bar item
		solo.clickOnActionBarItem(jackpal.androidterm.R.id.menu_toggle_wifilock);
        //Sleep for 692 milliseconds
		solo.sleep(692);
        //Click on (695.03467, 120.90554)
		solo.clickOnScreen(695.03467F, 120.90554F);
        //Sleep for 1536 milliseconds
		solo.sleep(536);
        //Click on action bar item
		solo.clickOnActionBarItem(jackpal.androidterm.R.id.menu_toggle_wifilock);
        //Sleep for 784 milliseconds
		solo.sleep(784);
        //Click on (677.05963, 134.8946)
		solo.clickOnScreen(677.05963F, 134.8946F);
        //Sleep for 1386 milliseconds
		solo.sleep(386);
        //Click on action bar item
		solo.clickOnActionBarItem(jackpal.androidterm.R.id.menu_toggle_wakelock);
        //Sleep for 2695 milliseconds
		solo.sleep(695);
        //Click on (221.6921, 115.81437)
		solo.clickOnScreen(221.6921F, 115.81437F);
	}
}
