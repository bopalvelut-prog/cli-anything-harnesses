import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def info(): click.echo('MakeMKV info')
@cli.command()
def rip(): click.echo('Ripping disc')
if __name__ == '__main__': cli()
