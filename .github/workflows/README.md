# GitHub Actions CI/CD Setup 🚀

This project uses GitHub Actions for automated testing, quality checks, and deployment.

## 📋 Workflows Overview

### 1. **simple-cicd.yml** (Recommended for beginners)
- **What it does**: Basic quality check + auto-deploy
- **When it runs**: On every push to main branch
- **Free tier usage**: ~2-5 minutes per run

### 2. **deploy.yml**
- **What it does**: Deploys your site to GitHub Pages
- **When it runs**: On push to main or manual trigger
- **Free tier usage**: ~1-2 minutes per run

### 3. **quality-check.yml**
- **What it does**: Validates HTML, checks CSS/JS, security scan
- **When it runs**: On all pushes and pull requests
- **Free tier usage**: ~5-10 minutes per run

### 4. **test-optimize.yml**
- **What it does**: Performance tests, accessibility checks, optimization
- **When it runs**: Weekly + on pushes
- **Free tier usage**: ~10-15 minutes per run

## 💰 Free Tier Calculation

With the free tier (2,000 minutes/month), you can run:

```
Simple CI/CD: 3 mins × 20 pushes/month = 60 minutes
Quality Check: 7 mins × 30 runs/month = 210 minutes
Test & Optimize: 12 mins × 8 runs/month = 96 minutes
-------------------------------------------
Total: 366 minutes/month (18% of free tier) ✅
```

## 🚀 Getting Started

### Step 1: Enable GitHub Actions
1. Push these workflow files to your repository
2. Go to your repo on GitHub
3. Click "Actions" tab
4. You'll see your workflows ready to run!

### Step 2: Enable GitHub Pages
1. Go to Settings → Pages
2. Source: "GitHub Actions"
3. Save

### Step 3: Make Your First Push
```bash
git add .
git commit -m "Add GitHub Actions workflows"
git push
```

## 📊 Monitoring Usage

Check your free tier usage:
1. Go to: https://github.com/settings/billing
2. Look for "Actions" section
3. See minutes used this month

## 🎯 Best Practices to Save Minutes

1. **Use workflow conditions**:
   ```yaml
   if: github.event_name == 'push' && github.ref == 'refs/heads/main'
   ```

2. **Cache dependencies**:
   ```yaml
   - uses: actions/cache@v3
     with:
       path: ~/.npm
       key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}
   ```

3. **Run on specific paths**:
   ```yaml
   on:
     push:
       paths:
         - '**.html'
         - '**.css'
         - '**.js'
   ```

4. **Use Ubuntu (1x multiplier) instead of Windows (2x) or macOS (10x)**

## 🔧 Workflow Controls

### Run Manually
1. Go to Actions tab
2. Select a workflow
3. Click "Run workflow"

### Cancel a Running Workflow
1. Go to Actions tab
2. Click on the running workflow
3. Click "Cancel workflow"

### Disable a Workflow
1. Go to Actions tab
2. Select the workflow
3. Click "..." → "Disable workflow"

## 📈 What Happens When You Hit the Limit?

- Workflows will pause until next month
- You'll get an email notification at 75% and 100%
- Options:
  - Wait for next month's reset
  - Upgrade to paid plan ($4/month for 3,000 minutes)
  - Use self-hosted runners (your own computer)

## 🛠️ Troubleshooting

### Workflow not running?
- Check if Actions is enabled in Settings
- Verify workflow file syntax (YAML is space-sensitive)
- Check branch names match

### Pages not deploying?
- Enable Pages in Settings
- Set source to "GitHub Actions"
- Wait 5-10 minutes for first deployment

### Permission errors?
- Check workflow permissions in Settings → Actions
- Ensure GITHUB_TOKEN has necessary permissions

## 💡 Tips

1. **Start simple**: Use `simple-cicd.yml` first
2. **Add gradually**: Enable other workflows as needed
3. **Monitor usage**: Check billing page weekly
4. **Learn from runs**: Click on workflow runs to see logs

---

## 🎉 You're All Set!

Your CI/CD pipeline is ready. Every push will now:
1. ✅ Check your code quality
2. 🚀 Deploy to GitHub Pages automatically
3. 📊 Give you feedback on any issues

Happy coding! 🎈