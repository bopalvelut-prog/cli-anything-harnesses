import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def forms(): click.echo('Google Forms')
@cli.command()
def responses(): click.echo('Google Forms responses')
if __name__ == '__main__': cli()
