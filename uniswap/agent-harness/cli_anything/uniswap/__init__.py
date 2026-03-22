import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def swap(): click.echo('Uniswap swap')
@cli.command()
def liquidity(): click.echo('Uniswap liquidity')
if __name__ == '__main__': cli()
