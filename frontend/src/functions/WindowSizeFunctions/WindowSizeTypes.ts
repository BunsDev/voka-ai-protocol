import { arrowMiddleware } from "element-plus";

/**
 * 根据屏幕的宽度，把屏幕分为不同尺寸类型
 */
export enum WindowSize {
    UNDEFINED = 0,
    TOOSMALL, //太小，无法适配
    TINY,
    SMALL,
    MIDDLE,
    LARGE,
    HUGE,
}

const size_threshold_value = {
    "tiny": 320, // 小屏手机
    "small": 414, // 大屏手机
    "middle": 1024, // 平板竖屏, ipad pro宽1024
    "large": 1280, // 平板横屏 or 笔记本
    "huge": 2048 // 显示器
}

export function computeWindowSizeByWidth(windowWidth: number): WindowSize {
    if(windowWidth < size_threshold_value["tiny"]) {
        return WindowSize.TOOSMALL;
    }
    if(windowWidth < size_threshold_value["small"]) {
        return WindowSize.TINY;
    }
    if(windowWidth < size_threshold_value["middle"]) {
        return WindowSize.SMALL;
    }
    if(windowWidth < size_threshold_value["large"]) { //ipad mini的宽度为768, ipad air宽度为820
        return WindowSize.MIDDLE; 
    }
    if(windowWidth <= size_threshold_value["huge"]) {// ipad air的高度为1180
        return WindowSize.LARGE;
    }
    return WindowSize.HUGE;
}