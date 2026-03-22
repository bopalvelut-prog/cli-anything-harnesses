import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def swap(): click.echo('SushiSwap swap')
@cli.command()
def pool(): click.echo('SushiSwap pool')
if __name__ == '__main__': cli()
