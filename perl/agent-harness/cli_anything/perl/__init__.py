import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('script')
def run(script): subprocess.run(['perl', script])
@cli.command()
def test(): subprocess.run(['prove', '-r', 't/'])
if __name__ == '__main__': cli()
