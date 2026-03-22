import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def vpa(): click.echo('Goldilocks VPA')
if __name__ == '__main__': cli()
