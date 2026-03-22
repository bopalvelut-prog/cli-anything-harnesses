import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def swap(): click.echo('PancakeSwap swap')
@cli.command()
def pool(): click.echo('PancakeSwap pool')
if __name__ == '__main__': cli()
