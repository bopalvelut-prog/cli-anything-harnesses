import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('url')
def crawl(url): subprocess.run(['katana', '-u', url])
@cli.command()
@click.argument('url')
def deep(url): subprocess.run(['katana', '-u', url, '-d', '3'])
if __name__ == '__main__': cli()
