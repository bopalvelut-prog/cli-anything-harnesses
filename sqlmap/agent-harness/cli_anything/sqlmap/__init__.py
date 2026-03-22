import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('url')
def scan(url): subprocess.run(['sqlmap', '-u', url])
@cli.command()
@click.argument('url')
@click.argument('param')
def test(url, param): subprocess.run(['sqlmap', '-u', url, '-p', param])
if __name__ == '__main__': cli()
