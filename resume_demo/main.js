// 初始化 AOS（卷軸動畫）
document.addEventListener('DOMContentLoaded', function(){
  AOS.init({ once:true, duration:700, offset:80 });

  // 初始化 fancybox（作品集燈箱）
  if (typeof $ !== 'undefined' && $.fancybox) {
    $("[data-fancybox='folio']").fancybox({
      loop:true,
      buttons:["zoom","slideShow","thumbs","close"],
      animationEffect:"zoom-in-out",
      transitionEffect:"fade"
    });
  }
});
