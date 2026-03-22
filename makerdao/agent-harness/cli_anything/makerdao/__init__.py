import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def vault(): click.echo('MakerDAO vault')
@cli.command()
def liquidate(): click.echo('MakerDAO liquidation')
if __name__ == '__main__': cli()
