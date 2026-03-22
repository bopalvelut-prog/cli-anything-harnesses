import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def swap(): click.echo('Raydium swap')
@cli.command()
def pool(): click.echo('Raydium pool')
if __name__ == '__main__': cli()
