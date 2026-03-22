import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def forms(): click.echo('Paperform forms')
@cli.command()
def submissions(): click.echo('Paperform submissions')
if __name__ == '__main__': cli()
