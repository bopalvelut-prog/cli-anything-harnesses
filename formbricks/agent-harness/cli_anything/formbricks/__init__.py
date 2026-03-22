import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def surveys(): click.echo('Formbricks surveys')
@cli.command()
def responses(): click.echo('Formbricks responses')
if __name__ == '__main__': cli()
