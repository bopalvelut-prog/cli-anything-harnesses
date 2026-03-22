import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def swap(): click.echo('Uniswap V3 swap')
@cli.command()
def pool(): click.echo('Uniswap V3 pool')
if __name__ == '__main__': cli()
